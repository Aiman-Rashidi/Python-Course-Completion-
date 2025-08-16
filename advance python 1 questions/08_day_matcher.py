def day_activity(day):
    match day.strip().lower():
        case "monday":
            return "Work begins!"
        case "saturday":
            return "Time to relax!"
        case "sunday":
            return "Family time!"
        case _:
            return "Unknown day!"
        
print(day_activity("   Monday   "))
print(day_activity("saturday"))
print(day_activity("   SuNDay   "))
print(day_activity(" random day "))