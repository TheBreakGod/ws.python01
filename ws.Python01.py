def calculate_target_heart_rate(age):
    mhr = 220 - age
    min_rate = int(0.6 * mhr)
    max_rate = int(0.7 * mhr)
    return min_rate, max_rate

age = int(input("โปรดระบุอายุปัจจุบันของคุณ"))
min_rate, max_rate = calculate_target_heart_rate(age)
print("ช่วงอัตตราเต้นของหัวใจที่เหมาะสมคือ {} - {} ครั้งต่อนาที".format(min_rate, max_rate))

    
