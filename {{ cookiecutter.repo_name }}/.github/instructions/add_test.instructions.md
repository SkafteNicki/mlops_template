---
applyTo: "tests/**/*.py"
---

# Testing Guidelines for MLOps Systems

The goal of testing in MLOps is **not** to verify model performance, but to ensure that
**data pipelines, models, and ML infrastructure behave correctly, reproducibly, and reliably**.

## Core Principles
- Use **pytest** as the primary testing framework
- Follow the **AAA pattern**: Arrange, Act, Assert
- Write **descriptive test names** that describe ML behavior
- Keep tests **fast, deterministic, and CI-friendly**
- Prefer **unit and lightweight integration tests** over full end-to-end training runs

---

## What to Test in an MLOps Context

### 1. Data
Focus on validating data contracts rather than values.

Test that:
- Input data has the expected **schema, shapes, and dtypes**
- Missing values and invalid inputs are handled correctly
- Feature ordering and naming are stable
- Preprocessing steps are **pure and deterministic**

Avoid:
- Using large or real datasets
- Asserting exact numerical values unless required

Example checks:
- DataFrame contains required columns
- No NaNs introduced after normalization
- Tokenization output length is consistent

---

### 2. Models
Tests should validate **model interfaces**, not model accuracy.

Test that models:
- Accept inputs of the expected shape and type
- Produce outputs of the expected shape and type
- Can be loaded from checkpoints or artifacts
- Fail gracefully on invalid input

Avoid:
- Training models inside tests
- Comparing exact floating-point outputs

---

### 3. Training Pipelines
Training pipelines should be tested on **small synthetic datasets**.

Test that:
- Pipelines run end-to-end on minimal data
- Configuration options are respected
- Expected artifacts (models, metrics, logs) are created
- Errors are raised for invalid configurations

Mock:
- GPU usage
- Long-running training loops
- External services

---

### 4. Reproducibility
Reproducibility is a core MLOps concern.

Test that:
- Random seeds are respected
- Deterministic components produce stable outputs
- Identical configurations yield equivalent results

Prefer:
- Comparing shapes, types, and ranges
- Tolerances for floating-point outputs

---

### 5. MLOps Infrastructure & Tooling
External systems must be mocked.

Mock interactions with:
- Experiment tracking (MLflow, Weights & Biases)
- Object storage (S3, GCS, Azure Blob)
- Databases and APIs

Test that:
- Metrics and artifacts are logged correctly
- Versioning information is recorded
- Failures (network, permissions) are handled properly

---

## Pytest Best Practices
- Use **fixtures** for:
  - Sample datasets
  - Models
  - Temporary directories
- Use **parametrized tests** for multiple input variants
- Keep all tests runnable on **CPU-only CI systems**
- Prefer **synthetic data** created inside the test

---

## Example: MLOps-Oriented Test

```python
import numpy as np
import pytest
from unittest.mock import patch

class TestInferencePipeline:
    @pytest.fixture
    def sample_batch(self):
        return np.random.rand(4, 10)

    @pytest.fixture
    def model(self):
        return load_model("tests/assets/dummy_model.pt")

    def test_model_inference_shape(self, model, sample_batch):
        # Act
        outputs = model.predict(sample_batch)

        # Assert
        assert outputs.shape == (4, 1)
        assert np.isfinite(outputs).all()

    @patch("src.tracking.log_metrics")
    def test_metrics_are_logged(self, mock_log_metrics, model, sample_batch):
        run_inference(model, sample_batch)
        mock_log_metrics.assert_called_once()
