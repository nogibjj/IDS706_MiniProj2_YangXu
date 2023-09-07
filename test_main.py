import main
import pandas as pd

def test_load_data():
    data = main.load_data()
    assert isinstance(data, pd.DataFrame)
    assert not data.empty

def test_get_descriptive_statistics():
    data = main.load_data()
    stats = main.get_descriptive_statistics(data)

    # Check if 'Product', 'Price', and 'Quantity' are in the columns
    assert "Product" not in stats.columns  # 'Product' shouldn't be in stats since it's non-numeric
    assert "Price" in stats.columns
    assert "Quantity" in stats.columns

    # Check if the stats such as 'count', 'mean', 'std', etc., are in the index.
    for stat in ["count", "mean", "std", "min", "25%", "50%", "75%", "max"]:
        assert stat in stats.index

