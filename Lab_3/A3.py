def main():
    prev_reading = int(input())
    curr_reading = int(input())

    if curr_reading >= prev_reading:
        used = curr_reading - prev_reading
    else:
        used = (10000 - prev_reading) + curr_reading

    total_cost = 0.0
    
    if used <= 300:
        total_cost = 21.0
    else:
        total_cost += 21.0
        
        if used <= 600:
            total_cost += (used - 300) * 0.06
        else:
            total_cost += 300 * 0.06
            
            if used <= 800:
                total_cost += (used - 600) * 0.04
            else:
                total_cost += 200 * 0.04
                
                total_cost += (used - 800) * 0.025

    if used > 0:
        avg_price = total_cost / used
    else:
        avg_price = 0.0

    print(f"{'Предыдущее':<14}{'Текущее':<11}{'Использовано':<16}{'К оплате':<12}{'Ср. цена m^3'}")
    print(f"   {prev_reading:<13}{curr_reading:<13}{used:<14}{total_cost:<14.2f}{avg_price:.2f}")

if __name__ == "__main__":
    main()
