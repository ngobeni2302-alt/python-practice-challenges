# ==============================================================================
# QUESTION 1: even_odd_tracker(numbers: list) -> list
# ==============================================================================

def even_odd_tracker(numbers: list) -> list:
    """Convert even/odd numbers to their string representations."""
    new_track = []
    odd = "Odd"
    even = "Even"
    new = {}
    for i in numbers:
        if i % 2 == 0:
            new_track.append(even)
        else:
            new_track.append(odd)
    #     for x in new_track:
    #         new[i] = x
    # return new
    return new_track
# print(even_odd_tracker([1,2,3,4]))

# ==============================================================================
# QUESTION 2: temperature_filter(temps: list) -> list
# ==============================================================================

def temperature_filter(temps: list) -> list:
    """Filter valid temperatures between 18-25 degrees."""
    return [temp for temp in temps if temp > 17 and temp < 26]

# print(temperature_filter([12,45,23,19,18,17,26,25]))


# ==============================================================================
# QUESTION 3: calculate_order_total(price: int, quantity: int) -> int
# ==============================================================================

def calculate_order_total(price: int, quantity: int) -> int:
    """Calculate order total with fees and minimum."""
    base = 10
    total = base + (price * quantity)  

    if quantity >= 5:
        total = total + 20

    if total < 50:
        total = 50  

    return total

# print(calculate_order_total(10, 2))


# ==============================================================================
# QUESTION 4: process_scores(scores: list) -> str
# ==============================================================================

def process_scores(scores: list) -> str:
    """Process scores and stop if any score is below 40."""
    for score in scores:
        if score < 40:
            return f"Stopped early at score {score}"
    return "All scores processed"

# print(process_scores([70,65, -6, 45]))


# ==============================================================================
# QUESTION 5: organize_products(items: list) -> dict
# ==============================================================================

def organize_products(items: list) -> dict:
    """Group products by their category."""
    new_items = {}

    for item in items:
        if item["category"] not in new_items:
            new_items[item["category"]] = []
        new_items[item["category"]].append(item["name"])
    return new_items

# print(organize_products([
#   {"name": "Milk", "category": "Dairy"},
#   {"name": "Cheese", "category": "Dairy"},
#   {"name": "Milk", "category": "Carbon"},
#   {"name": "Cheese", "category": "Dairy"}
# ]))

# ==============================================================================
# QUESTION 6: sequence_growth(nums: list) -> int
# ==============================================================================

def sequence_growth(nums: list) -> int:
    """Find the longest strictly increasing consecutive sequence."""
    pass
