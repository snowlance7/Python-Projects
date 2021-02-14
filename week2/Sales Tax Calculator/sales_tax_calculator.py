import stcUI_module
import stcTax_module

print("Sales Tax Calculator")

def main():
    total = stcUI_module.get_input()
    stcUI_module.display_total(total)
    stcUI_module.display_sales_tax(stcTax_module.sales_tax(total))
    stcUI_module.display_total_after_tax(stcTax_module.total_after_tax(total))

    if input("\nAgain? (y/n): ").lower() == "y":
        main()
    else:
        print("\nThanks, bye!")


if __name__ == "__main__":
    main()