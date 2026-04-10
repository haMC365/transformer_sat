def train(model, dataloader, optimizer, criterion):
    model.train()

    for x, y in dataloader:
        optimizer.zero_grad()
        output = model(x)
        loss = criterion(output, y)
        loss.backward()
        optimizer.step()
