from fib import *
# from fib import *
import json
def test(fun,testCaseArray,expectedResultArray):
    failCount = 0
    passCount = 0
    errorCount = 0
    failArray = []
    passArray = []
    errorCaseArray = {}
    for i in range(len(testCaseArray)):
        try:
            assert fun(testCaseArray[i]) == expectedResultArray[i]
            passCount += 1
            passArray.append(testCaseArray[i])
        except AssertionError:
            failCount += 1
            failArray.append(testCaseArray[i])
        except Exception as e:
            errorCount += 1
            errorCaseArray[testCaseArray[i]] = str(e)
    # print("Passed: ",passCount,"/",len(testCaseArray))
    # print("Failed: ",failCount,"/",len(testCaseArray))
    # print("Error: ",errorCount,"/",len(testCaseArray))
    # print("Passed: ",passArray)
    # print("Failed: ",failArray)
    # print("\nErrors:")
    for i in errorCaseArray:
        print("Faced "+str(errorCaseArray[i])+" when testing "+str(i))
    with open ("test.json", "w") as f:
        json.dump({
            "passed": passCount,
            "failed": failCount,
            "error": errorCount,
            "passed_cases": passArray,
            "failed_cases": failArray,
            "error_cases": errorCaseArray
        }, f,indent=4)

# test(fib, [0,1,-1,-2,5], [0,1,-1,-2,3])


test(fib,[0,1,-1,-2,5],[0,1,-1,-2,3])