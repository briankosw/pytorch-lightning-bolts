"""
Test Object Detection Loss Functions
"""

import pytest
import torch

from pl_bolts.losses.object_detection import giou_loss


@pytest.mark.parametrize(
    "pred, target, expected_loss",
    [
        (
            torch.tensor([[100, 100, 200, 200]]),
            torch.tensor([[100, 100, 200, 200]]),
            torch.tensor([0.0]),
        )
    ],
)
def test_complete_overlap(pred, target, expected_loss):
    torch.testing.assert_allclose(giou_loss(pred, target), expected_loss)


@pytest.mark.parametrize(
    "pred, target, expected_loss",
    [
        (
            torch.tensor([[100, 100, 200, 200]]),
            torch.tensor([[100, 200, 200, 300]]),
            torch.tensor([1.0]),
        ),
        (
            torch.tensor([[100, 100, 200, 200]]),
            torch.tensor([[200, 200, 300, 300]]),
            torch.tensor([1.5]),
        ),
    ],
)
def test_no_overlap(pred, target, expected_loss):
    torch.testing.assert_allclose(giou_loss(pred, target), expected_loss)
