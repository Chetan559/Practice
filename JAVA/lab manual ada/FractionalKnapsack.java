import java.util.Arrays;
import java.util.Comparator;

class Item {
    double weight;
    double value;

    public Item(double weight, double value) {
        this.weight = weight;
        this.value = value;
    }
}

class FractionalKnapsack {
    // Function to calculate the maximum value we can fit in the knapsack
    public static double getMaxValue(Item[] items, double capacity) {
        // Sorting items by value-to-weight ratio in decreasing order
        Arrays.sort(items, new Comparator<Item>() {
            @Override
            public int compare(Item i1, Item i2) {
                double ratio1 = i1.value / i1.weight;
                double ratio2 = i2.value / i2.weight;
                return Double.compare(ratio2, ratio1); // Sort in descending order
            }
        });

        double totalValue = 0.0; // Total value in knapsack
        double currentWeight = 0.0; // Current weight of knapsack

        // Iterate through all items
        for (Item item : items) {
            // If the item can be added completely
            if (currentWeight + item.weight <= capacity) {
                currentWeight += item.weight;
                totalValue += item.value;
            } else {
                // If only part of the item can be added
                double remainingCapacity = capacity - currentWeight;
                totalValue += item.value * (remainingCapacity / item.weight);
                break; // No more items can be added, so we break
            }
        }

        return totalValue;
    }

    public static void main(String[] args) {
        // Input: weights and values of items
        Item[] items = {
            new Item(10, 60),
            new Item(20, 100),
            new Item(30, 120)
        };

        double capacity = 50.0; // Maximum capacity of knapsack

        // Calculate and print the maximum value we can get
        double maxValue = getMaxValue(items, capacity);
        System.out.println("Maximum value in Knapsack = " + maxValue);
    }
}
