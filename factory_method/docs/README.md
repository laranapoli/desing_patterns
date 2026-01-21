# Factory Method (FM) Pattern

## 1st Variant: The classic of original GoF FM

- Para cada tipo de objeto concreto precisamos de uma implementação concentra de uma FM para o criar!
- Aqui temos uma interface para a factory

![classic](image.png)

![classic-UML](image-1.png)

## 2nd Variant: The simple method variand - Parameterized FM

- GRANDE DIFERENCA: Aqui NÃO temos uma interface para a factory
- 1 Factory - Multiple instances
    - Private constructor: Não podemos instanciar a factory
    - Static method: create instance (recebe um parâmetro que pode ser qualquer coisa)

![parameterized](image-2.png)


![parameterized-UML](image-3.png)

### Improvement

- Jeito melhor de pssar dados para um FM: Permite + flexibilidade
- Context class: Agrega dados necessários para criar objeto. Usa como input para o método de criação

![improvement](image-4.png)

- Maneira de resolver o problema do if else com strings: ENUMERATION!!

![ENUM](image-5.png)

# Exercises

![1](image-6.png)

![2](image-7.png)