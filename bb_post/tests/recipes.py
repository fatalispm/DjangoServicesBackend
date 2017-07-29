from django.contrib.auth import get_user_model
from model_mommy.recipe import Recipe

UserRecipe = Recipe(get_user_model())