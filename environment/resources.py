class Resources:
    def __init__(self):
        self.global_resources = {
            "food": 1000,
            "money": 5000,
            "water": 2000
        }

    def allocate(self, resource, amount):
        """Allocates resources if available."""
        if self.global_resources.get(resource, 0) >= amount:
            self.global_resources[resource] -= amount
            return amount
        return 0

    def replenish(self, resource, amount):
        """Replenishes the world's resources."""
        if resource in self.global_resources:
            self.global_resources[resource] += amount

    def get_status(self):
        """Returns the current resource levels."""
        return self.global_resources

    def __str__(self):
        return f"Resources: {self.global_resources}"
