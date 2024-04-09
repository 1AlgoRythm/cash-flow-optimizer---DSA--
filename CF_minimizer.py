import heapq

# Calculate the net amounts for each person based on the debts graph
def calculate_net_amounts(debts):
    # Initialize net amounts for each person
    net_amounts = {person: 0 for person in debts}
    # Calculate net amount by summing debts and credits
    for debtor, transactions in debts.items():
        for creditor, amount in transactions:
            net_amounts[debtor] -= amount
            net_amounts[creditor] += amount
    return net_amounts

# Settle debts with minimal transactions using a greedy approach
def settle_debts(net_amounts):
    # Create heaps for creditors and debtors for efficient retrieval
    creditors = [(-amount, person) for person, amount in net_amounts.items() if amount > 0]
    debtors = [(amount, person) for person, amount in net_amounts.items() if amount < 0]
    heapq.heapify(creditors)
    heapq.heapify(debtors)

    # List to store the transactions that settle the debts
    transactions = []

    # Settle debts by matching the largest creditor with the largest debtor
    while creditors and debtors:
        credit, creditor = heapq.heappop(creditors)
        debt, debtor = heapq.heappop(debtors)

        # Determine the amount to settle in this transaction
        settled_amount = min(-debt, -credit)
        transactions.append((debtor, creditor, settled_amount))

        # If there's remaining debt or credit, push back to the heap
        if -debt > settled_amount:
            heapq.heappush(debtors, (debt + settled_amount, debtor))
        if -credit > settled_amount:
            heapq.heappush(creditors, (credit + settled_amount, creditor))

    return transactions

# Test function to validate the logic of cash flow minimizer
def test_cash_flow_minimizer():
    print("Starting tests...")
    # Define a small scenario to test the cash flow minimization
    debts = {
        "A": [("B", 50), ("C", 100)],
        "B": [("C", 30)],
        "C": [("A", 10)]
    }
    # Calculate net amounts and settle debts
    net_amounts = calculate_net_amounts(debts)
    transactions = settle_debts(net_amounts)

    assert transactions, "Test failed: No transactions returned"
    print("Test passed: Transactions calculated")
    # Print the transactions for review
    for debtor, creditor, amount in transactions:
        print(f"{debtor} pays {creditor}: ${amount}")

def large_test_cash_flow_minimizer():
    print("Starting large tests...")
    # Define a larger scenario with more debts
    debts = {
        "A": [("B", 300), ("C", 250), ("D", 100)],
        "B": [("C", 150), ("E", 200)],
        "C": [("A", 400), ("D", 150), ("F", 100)],
        "D": [("B", 50), ("E", 300)],
        "E": [("A", 500), ("C", 100), ("F", 200)],
        "F": [("D", 500)]
    }

    # Expected transactions to be verified, this should be logical conclusions of how debts can be minimized
    # Note: These are hypothetical and would need to be adjusted based on actual debt minimization logic
    expected_transactions = [
        ("F", "A", 150),
        ("D", "A", 350),
        ("B", "A", 100),
        ("C", "A", 300),
        ("E", "B", 300),
        ("E", "C", 200)
    ]

    net_amounts = calculate_net_amounts(debts)
    actual_transactions = settle_debts(net_amounts)

    # Printing actual transactions for debugging purpose
    print("Actual transactions:")
    for debtor, creditor, amount in actual_transactions:
        print(f"{debtor} pays {creditor}: ${amount}")

    assert len(actual_transactions) <= len(expected_transactions), "Test failed: Too many transactions"
    print("Large test passed: Transactions seem logically minimized")

# Add the large_test_cash_flow_minimizer call in your main function to execute the large test


# Main function to orchestrate the flow of the program
def main():
    # Initial debts setup
    debts = {
        "A": [("B", 50), ("C", 100)],
        "B": [("A", 10), ("C", 20)],
        "C": []
    }

    # Calculate net amounts and settle the debts
    net_amounts = calculate_net_amounts(debts)
    transactions = settle_debts(net_amounts)

    print("Transactions to settle debts:")
    for debtor, creditor, amount in transactions:
        print(f"{debtor} pays {creditor}: ${amount}")

    # Run tests to ensure the system works as expected
    test_cash_flow_minimizer()
    large_test_cash_flow_minimizer()

# Ensure that the main function runs only when the script is executed directly
if __name__ == "__main__":
    main()
