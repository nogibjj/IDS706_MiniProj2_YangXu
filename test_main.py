import main
import pandas as pd

def test_load_data():
    data = main.load_data()
    assert isinstance(data, pd.DataFrame)
    assert not data.empty

def test_get_descriptive_statistics():
    data = main.load_data()
    stats = main.get_descriptive_statistics(data)

    # We know the dataset_sample.csv has 'Product', 'Price', and 'Quantity' columns.
    # We'll make some basic assertions based on these.

    assert "Product" in stats.index
    assert "Price" in stats.columns
    assert "Quantity" in stats.columns

    # Check some basic stats
    assert stats.loc["count", "Price"] == 9
    assert stats.loc["count", "Quantity"] == 9
    assert stats.loc["mean", "Price"] == (1.2 + 0.5 + 2.5 + 1.3 + 0.6 + 2.4 + 1.1 + 0.7 + 2.6) / 9
    assert stats.loc["mean", "Quantity"] == (50 + 40 + 20 + 45 + 50 + 22 + 55 + 42 + 19) / 9
    assert stats.loc["min", "Price"] == 0.5
    assert stats.loc["min", "Quantity"] == 19
    assert stats.loc["max", "Price"] == 2.6
    assert stats.loc["max", "Quantity"] == 55
