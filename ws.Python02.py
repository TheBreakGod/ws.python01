def calculate_grass_cutting_cost(width, length, rate_per_sqm):
    area = width * length
    total_cost = area * rate_per_sqm
    return total_cost

x = float(input("โปรดระบุความกว้างของสนามหญ้า (เมตร)"))
y = float(input("โปรดระบุความยาวของสนามหญ้า (เมตร)"))
b = float(input("โปรดระบุราคาหญ้าต่อตารางเมตร (บาท)"))

total_cost = calculate_grass_cutting_cost(x,y,b)
print("ราคาตัดหญ้าทั้งหมดคือ {:.2f} บาท ".format(total_cost))
