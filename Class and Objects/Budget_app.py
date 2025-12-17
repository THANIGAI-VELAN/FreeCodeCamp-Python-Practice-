class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = self.name.center(30, "*")
        lines = [title]

        for item in self.ledger:
            desc = item["description"][:23].ljust(23)
            amt = f"{item['amount']:.2f}".rjust(7)
            lines.append(desc + amt)

        lines.append(f"Total: {self.get_balance():.2f}")
        return "\n".join(lines)


def create_spend_chart(categories):
    chart = "Percentage spent by category\n"

    # Calculate spent amounts
    spent = []
    for cat in categories:
        total = 0
        for item in cat.ledger:
            if item["amount"] < 0:
                total += -item["amount"]
        spent.append(total)

    total_spent = sum(spent)

    # Percentages rounded DOWN to nearest 10
    percentages = []
    for s in spent:
        p = int((s / total_spent) * 100)
        percentages.append(p - (p % 10))

    # Bar chart
    for i in range(100, -1, -10):
        chart += str(i).rjust(3) + "| "
        for p in percentages:
            chart += "o  " if p >= i else "   "
        chart += "\n"

    # Horizontal line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Vertical labels (⚠️ NO stripping spaces)
    names = [cat.name for cat in categories]
    max_len = max(len(name) for name in names)

    for i in range(max_len):
        chart += "     "
        for name in names:
            if i < len(name):
                chart += name[i] + "  "
            else:
                chart += "   "
        if i < max_len - 1:
            chart += "\n"

    return chart
