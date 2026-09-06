class PointDatabase:
    def __init__(self, pointlist):
        def f(l):
            return l[0]
        pointlist.sort(key = f)
        self.object = pointlist
    
    def searchNearby(self, q, d):
        output = []
        x_interval = [q[0] - d, q[0] + d]
        y_interval = [q[1] - d, q[1] + d]
        def binary_search(arr, a, b):
            def lower(arr, low, high, a, b):
                mid = (high + low) // 2
                if a < arr[mid][0]:
                    if mid != low:
                        if not (a < arr[mid - 1][0]):
                            return mid
                        else:
                            return lower(arr, low, mid - 1, a, b)
                    else:
                        return mid
                else:
                    return lower(arr, mid + 1, high, a, b)

            def higher(arr, low, high, a, b):
                mid = (high + low) // 2
                if arr[mid][0] < b:
                    if mid != high:
                        if not (arr[mid + 1][0] < b):
                            return mid
                        else:
                            return higher(arr, mid + 1, high, a, b)
                    else:
                        return mid
                else:
                    return higher(arr, low, mid - 1, a, b)

            aa = lower(arr, 0, len(arr)-1, a, b)
            bb = higher(arr, 0, len(arr)-1, a, b)
            if aa <= bb:
                return [aa, bb]
            else:
                return None
        if len(self.object) != 0:
            xx = binary_search(self.object, x_interval[0], x_interval[1])
            if xx != None:
                for i in range(xx[0], xx[1] + 1):
                    if y_interval[0] < self.object[i][1] < y_interval[1]:
                        output.append(self.object[i])
        return output