import json
from scripts.parse_json import sanitize_numeric_field

# Create test JSON with NaN values
test_recipes_with_nan = [
    {
        "cuisine": "Italian", 
        "title": "Test Recipe 1",
        "rating": "NaN",  # String NaN
        "prep_time": "nan",  # Lowercase nan
        "cook_time": 30,
        "total_time": 60,
        "description": "Test recipe with NaN rating",
        "nutrients": {"calories": "400 kcal"},
        "serves": "4 servings"
    },
    {
        "cuisine": "Mexican",
        "title": "Test Recipe 2", 
        "rating": 4.5,
        "prep_time": "",  # Empty string
        "cook_time": "NaN",  # String NaN
        "total_time": "invalid",  # Invalid string
        "description": "Test recipe with various NaN values",
        "nutrients": {"calories": "350 kcal"},
        "serves": "2 servings"
    },
    {
        "cuisine": "Asian",
        "title": "Test Recipe 3",
        "rating": None,  # None value
        "prep_time": 15,
        "cook_time": 25,
        "total_time": 40,
        "description": "Test recipe with None rating", 
        "nutrients": {"calories": "300 kcal"},
        "serves": "6 servings"
    }
]

# Save test data
with open('test_recipes_nan.json', 'w') as f:
    json.dump(test_recipes_with_nan, f, indent=2)

print("✅ Created test_recipes_nan.json with NaN values")
print("🧪 Run: python scripts/parse_json.py test_recipes_nan.json")

# Test the sanitization function
print("\n🔬 Testing NaN sanitization:")
for recipe in test_recipes_with_nan:
    print(f"\nRecipe: {recipe['title']}")
    print(f"  Rating: {recipe['rating']} → {sanitize_numeric_field(recipe['rating'])}")
    print(f"  Prep: {recipe['prep_time']} → {sanitize_numeric_field(recipe['prep_time'])}")
    print(f"  Cook: {recipe['cook_time']} → {sanitize_numeric_field(recipe['cook_time'])}")
    print(f"  Total: {recipe['total_time']} → {sanitize_numeric_field(recipe['total_time'])}")
