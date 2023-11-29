import json

# Carregar e analisar o JSON do arquivo externo
with open('business_rules.json', 'r') as file:
    rules = json.load(file)


def apply_rule(rule_name, order_amount):
    for rule in rules:
        if rule['ruleName'] == rule_name:
            print(f"Aplicando a regra: {rule_name}")
            if order_amount > rule["conditions"]["orderValue"]["greaterThan"]:
                if rule["actions"]["applyFreeShipping"]:
                    print("Frete grátis aplicado.")
                    return True
            print("Frete não aplicado.")
            return False
    print("Regra não encontrada.")
    return False


# Exemplo de uso da regra
order_value = 600
apply_rule("Frete Gratis", order_value)
