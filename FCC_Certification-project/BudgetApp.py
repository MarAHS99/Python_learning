class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False
        self.ledger.append({'amount': -amount, 'description': description})
        return True

    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item['amount']
        return total

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False
        self.withdraw(amount, f"Transfer to {category.name}")
        category.deposit(amount, f"Transfer from {self.name}")
        return True

    def __str__(self):
        title = self.name.center(30, "*") + "\n"
        items = ""
        for entry in self.ledger:
            desc = entry['description'][:23]
            amt = "{:.2f}".format(entry['amount'])
            items += f"{desc:<23}{amt:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    total_spent = 0
    spent_per_category = []

    for category in categories:
        spent = 0
        for entry in category.ledger:
            if entry['amount'] < 0:
                spent += -entry['amount']
        spent_per_category.append(spent)
        total_spent += spent

    percentages = []
    for spent in spent_per_category:
        percent = int((spent / total_spent) * 100)
        percent = percent - (percent % 10)
        percentages.append(percent)

    chart = "Percentage spent by category\n"

    for i in range(100, -1, -10):
        chart += f"{i:>3}| "
        for p in percentages:
            if p >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_len = max(len(cat.name) for cat in categories)

    for i in range(max_len):
        chart += "     "
        for cat in categories:
            if i < len(cat.name):
                chart += cat.name[i] + "  "
            else:
                chart += "   "
        if i != max_len - 1:
            chart += "\n"

    return chart
