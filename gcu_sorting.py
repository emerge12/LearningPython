
import os
# Sort through folder

# Failure by station
Station_1 = 0
Station_2 = 0
Station_3 = 0
unitCountPerTest = []
percentage_fail_per_unit = []
fails_with_1_unit = 0
fails_with_2_unit = 0
fails_with_3_unit = 0
percentage_fails_with_1_unit = []
percentage_fails_with_2_unit = []
percentage_fails_with_3_unit = []

gpu_test_log_dir = "X:\\HG-JCTS (Harpoon GCU)\\LogFiles\\GCU"
with open("gcu_cnd_serial_numbers.txt", "r") as gcu_data:
    for line in gcu_data:
        count = 0
        unit_count = 0
        test_file_log_path = gpu_test_log_dir + "\\" + line[4:10] + "\\" + line.strip()
        with open(test_file_log_path,"r", errors = "ignore") as testlog:
            with open("gcu_analysis_result.txt", "a") as f:
                f.write("GCU_" + line[4:10])
                for testline in testlog:
                    count +=1
                    if count >= 17 and count <= 20:
                        if testline.find("Serial") == -1:
                            f.write("  " + testline.strip())
                            if testline.find("Station Number: 1") != -1:
                                Station_1 += 1
                            if testline.find("Station Number: 2") != -1:
                                Station_2 += 1
                            if testline.find("Station Number: 3") != -1:
                                Station_3 += 1
                            # Check for additional in Thermothron 
                            if testline.find("N/A") == -1 and testline.find("Station Number") == -1 and testline.find(line[4:10]) == -1:
                                unit_count += 1
                            #print(testline) 
                if unit_count == 0:
                    fails_with_1_unit +=1
                if unit_count == 1:
                    fails_with_2_unit +=1
                if unit_count == 2:
                    fails_with_3_unit +=1
                
                unitCountPerTest.append("GCU_" + line[4:10] +" tested with " + str(unit_count) + " other unit(s).")                
                f.write("\n")
               


# Perform data analysis

total_fail =  Station_2 + Station_1 + Station_3


with open("cnd_gcu_analysis_result2.txt", "a")as result:
    print("\n")
    print("*********************** PERCENTAGE OF FAILURES BY STATION **************************************")
    result.write("************************* PERCENTAGE OF FAILURES BY STATION ********************************\n")    
    print("Percentage of failure on Staion 1: " + str(round((Station_1/total_fail)*100,2)) + "%")
    print("Percentage of failure on Staion 2: " + str(round((Station_2/total_fail)*100,2)) + "%")
    print("Percentage of failure on Staion 3: " + str(round((Station_3/total_fail)*100,2)) + "%")
    result.write("Percentage of failure on Staion 1: " + str(round((Station_1/total_fail)*100,2)) + "%\n")
    result.write("Percentage of failure on Staion 2: " + str(round((Station_2/total_fail)*100,2)) + "%\n")
    result.write("Percentage of failure on Staion 3: " + str(round((Station_3/total_fail)*100,2)) + "%\n")
    print("\n")
    result.write("\n")


    print("**************************** NUMBER OF UNIT TESTED WITH FAILED GCU **************************************")
    result.write("*********************** PERCENTAGE OF FAILURES BY STATION **************************************\n")
    for index in unitCountPerTest:
        print(index)
        result.write(index + "\n")
    result.write("\n")
    print("\n")


    print("*********************** PERCENTAGE OF FAILURE PER UNIT TESTED **************************************")
    result.write("*********************** PERCENTAGE OF FAILURE PER UNIT TESTED **************************************\n")
    percentage_fails_with_1_unit.append(str(round((fails_with_1_unit/total_fail)*100,2)) + "% failure occur when only one unit is tested")
    for index in percentage_fails_with_1_unit:
        print(index)
        result.write(index + "\n")


    percentage_fails_with_2_unit.append(str(round((fails_with_2_unit/total_fail)*100,2)) + "% failure occur when two unit is tested")
    for index in percentage_fails_with_2_unit:
        print(index)
        result.write(index + "\n")


    percentage_fails_with_3_unit.append(str(round((fails_with_3_unit/total_fail)*100,2)) + "% failure occur when three unit is tested")
    for index in percentage_fails_with_3_unit:
        print(index)
        result.write(index + "\n")
    print("\n")
    # Summerize Results          