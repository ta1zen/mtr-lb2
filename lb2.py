import math

corporations = {
    'Corporation 1': {
        'success_prob': 0.6,
        'success_profit': 10_000_000,
        'failure_prob': 0.4,
        'failure_profit': 500_000
    },
    'Corporation 2': {
        'success_prob': 0.4,
        'success_profit': 10_000_000,
        'failure_prob': 0.6,
        'failure_profit': 1_000_000
    }
}

def calculate_metrics(success_prob, success_profit, failure_prob, failure_profit):
    expected_profit = success_prob * success_profit + failure_prob * failure_profit
    
    variance = (success_prob * (success_profit - expected_profit) ** 2 + 
                failure_prob * (failure_profit - expected_profit) ** 2)
    
    std_dev = math.sqrt(variance)
    
    coefficient_of_variation = std_dev / expected_profit
    
    semi_variance = failure_prob * (min(0, failure_profit - expected_profit) ** 2)
    semi_std_dev = math.sqrt(semi_variance)
    
    return expected_profit, std_dev, coefficient_of_variation

metrics = {}

for name, data in corporations.items():
    expected_profit, std_dev, coefficient_of_variation = calculate_metrics(
        data['success_prob'], data['success_profit'], data['failure_prob'], data['failure_profit'])
    
    metrics[name] = {
        'Expected Profit': expected_profit,
        'Standard Deviation': std_dev,
        'Coefficient of Variation': coefficient_of_variation,
    }
    
    print(f"Metrics for {name}:")
    print(f"  Expected Profit: ${expected_profit / 1_000_000:.2f} million")
    print(f"  Standard Deviation: ${std_dev / 1_000_000:.2f} million")
    print(f"  Coefficient of Variation: {coefficient_of_variation:.2f}")

corp1_metrics = metrics['Corporation 1']
corp2_metrics = metrics['Corporation 2']

if corp1_metrics['Coefficient of Variation'] < corp2_metrics['Coefficient of Variation']:
    print (f"Оскільки корпорація 1 має нижчий коефіцієнт варіації "
                      f"({corp1_metrics['Coefficient of Variation'] * 100:.2f}%) це свідчить про те, що корпорація 1 "
                      "є менш ризикованою відносно свого очікуваного прибутку."
                      " Тому інвестиції в корпорацію 1 виглядають привабливішими як з точки зору очікуваного прибутку, так і з точки зору ризику.")
elif corp1_metrics['Coefficient of Variation'] > corp2_metrics['Coefficient of Variation']:
    recommendation = (f"Оскільки корпорація 2 має нижчий коефіцієнт варіації "
                      f"({corp2_metrics['Коефіцієнт варіації'] * 100:.2f}%) це свідчить про те, що корпорація 2 "
                      "є менш ризикованою відносно свого очікуваного прибутку."
                        " Тому інвестиції в корпорацію 2 виглядають привабливішими як з точки зору очікуваного прибутку, так і з точки зору ризику.")