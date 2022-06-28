from arithmetic_arranger import arithmetic_arranger

print("Testcase 1: Correct arguments.")
arithmetic_arranger(["4 + 9", "20 - 50", "8504 - 8", "200 - 85", "578 + 599"], True)
arithmetic_arranger(["5 - 6", "9 - 7"])
print("Testcase 2: Too many problems.")
arithmetic_arranger(["4 + 9", "20 - 50", "8504 - 8", "59 - 87", "200 - 85", "578 + 599"])
print("Testcase 3: Non-numeric value.")
arithmetic_arranger(["f + 4", "45 - 19"])
print("Testcase 4: Wrong operator.")
arithmetic_arranger(["4 * 3"])
print("Testcase 5: Too many digits.")
arithmetic_arranger(["80 - 9", "55596 + 156", "578 + 68"], True)
