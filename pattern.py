def analyze_temperature_pattern(temperatures):
    """
    Analyze temperature data to find patterns
    - Daily variations
    - Weekly trends
    - Seasonal changes
    """
    # Calculate daily average change
    daily_changes = [temperatures[i+1] - temperatures[i] 
                    for i in range(len(temperatures)-1)]
    avg_change = sum(daily_changes) / len(daily_changes)
    
    # Find cycles (weekly pattern for 7-day data)
    if len(temperatures) >= 7:
        weekly_pattern = temperatures[:7]
        print(f"Weekly pattern: {weekly_pattern}")
    
    # Detect anomalies (temperatures significantly different from average)
    avg_temp = sum(temperatures) / len(temperatures)
    std_dev = (sum((t - avg_temp) ** 2 for t in temperatures) / len(temperatures)) ** 0.5
    
    anomalies = [temp for temp in temperatures 
                if abs(temp - avg_temp) > 2 * std_dev]
    
    print(f"Average temperature: {avg_temp:.2f}°F")
    print(f"Average daily change: {avg_change:+.2f}°F")
    print(f"Standard deviation: {std_dev:.2f}°F")
    if anomalies:
        print(f"Anomalies detected: {anomalies}")
    
    return avg_temp, avg_change, anomalies

# Test with sample data
temps = [72, 75, 73, 70, 68, 71, 74, 76, 78, 75, 73, 95, 72, 74]
analyze_temperature_pattern(temps)