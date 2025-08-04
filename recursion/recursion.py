count = 0
def fun():
    global count
    if count > 4:
        return
    print("P")
    count += 1
    fun()
fun()