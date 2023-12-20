def cal_income(class_a_tickets, class_b_tickets, class_c_tickets):
    income = (class_a_tickets * 20) + (class_b_tickets * 15) + (class_c_tickets * 10)
    return income
def main():
    class_a_tickets = int(input("Enter the number of Class A tickets sold: "))
    class_b_tickets = int(input("Enter the number of Class B tickets sold: "))
    class_c_tickets = int(input("Enter the number of Class C tickets sold: "))
    total_income = cal_income(class_a_tickets, class_b_tickets, class_c_tickets)
    print(f"Total Income from Ticket Sales: ${total_income}")
if __name__ == "__main__":
    main()
