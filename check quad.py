def euler_criterion(x, m):
    # Kiểm tra x^((m-1)/2) mod m có bằng 1 không
    power = pow(x, (m - 1) // 2, m)
    return power == 1

# Số cần kiểm tra và số modulo
x_value = 6
m = 29

# Kiểm tra xem x_value có phải là quadratic residue modulo m không
is_quadratic_residue = euler_criterion(x_value, m)

if is_quadratic_residue:
    print(f"{x_value} là quadratic residue modulo {m}.")
else:
    print(f"{x_value} không phải là quadratic residue modulo {m}.")