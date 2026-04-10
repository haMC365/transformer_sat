def evaluate(model, dataloader):
    model.eval()
    correct = 0

    with torch.no_grad():
        for x, y in dataloader:
            pred = model(x)
            correct += ((pred > 0.5) == y).sum().item()

    return correct / len(dataloader.dataset)
