import torch.nn as nn


class SATTransformer(nn.Module):
    def __init__(self, input_dim, d_model=64, nhead=4):
        super().__init__()

        self.embedding = nn.Linear(input_dim, d_model)
        self.transformer = nn.TransformerEncoder(
            nn.TransformerEncoderLayer(d_model, nhead), num_layers=2
        )
        self.fc = nn.Linear(d_model, 1)

    def forward(self, x):
        x = self.embedding(x)
        x = self.transformer(x)
        x = x.mean(dim=1)
        return self.fc(x)
