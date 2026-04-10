import torch


class MultiAgentSystem:
    def __init__(self, models):
        self.models = models

    def predict(self, x):
        outputs = [model(x) for model in self.models]
        return torch.mean(torch.stack(outputs), dim=0)
