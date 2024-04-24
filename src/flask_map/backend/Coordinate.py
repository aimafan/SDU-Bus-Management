# 各个公交站点的坐标
import math
import bisect
from flask_map.myutils.config import config

speed = int(config["bus"]["speed"])


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def distance_to(self, other):
        """
        计算当前坐标到另一个坐标的距离
        :param other: 另一个 Coordinate 对象
        :return: 两个坐标之间的距离
        """
        dx = self.x - other.x
        dy = self.y - other.y
        distance = math.sqrt(dx**2 + dy**2)
        return distance


class Route:
    def __init__(self):
        self.coordinates = []
        self.distance = []

    def add_ordered_coordinate(self, coordinate: Coordinate):
        """
        添加一个有序的站点到路线中
        :param coordinate: 要添加的 Coordinate 对象
        """
        self.coordinates.append(coordinate)
        if len(self.coordinates) <= 1:
            self.distance.append(0)
        else:
            delta_distance = coordinate.distance_to(self.coordinates[-2])
            delta_distance += self.distance[-1]
            self.distance.append(delta_distance)

    def calculate_coordinate(self, distance):
        """
        计算距离起始点distance的结点的坐标
        """
        if distance == 0:
            return self.coordinates[0]
        position = bisect.bisect_left(self.distance, distance)

        coord_a = self.coordinates[position - 1]
        coord_b = self.coordinates[position]

        segment_length = coord_a.distance_to(coord_b)

        alpha = (distance - self.distance[position - 1]) / segment_length

        # 使用线性插值计算结点 C 的坐标
        coord_c_x = coord_a.x + alpha * (coord_b.x - coord_a.x)
        coord_c_y = coord_a.y + alpha * (coord_b.y - coord_a.y)

        return Coordinate(int(coord_c_x), int(coord_c_y))

    def calculate_time(self, distance):
        dis = []
        position = bisect.bisect_left(self.distance, distance)
        for i in range(position, len(self.distance)):
            dis.append(
                [self.coordinates[i], round((self.distance[i] - distance) / speed, 2)]
            )

        return dis

    def is_out_distance(self, distance):
        """
        计算是否超过了最大距离
        """
        if distance > self.distance[-1]:
            # 超过了最大距离
            return True
        return False


def out_distance(line, distance):
    if distance < 0:
        return True
    if line == "1":
        return line1.is_out_distance(distance)
    if line == "2":
        return line2.is_out_distance(distance)
    if line == "3":
        return line3.is_out_distance(distance)
    if line == "4":
        return line4.is_out_distance(distance)


def get_time_list(line, distance):
    if line == "1":
        return line1.calculate_time(distance)
    if line == "2":
        return line2.calculate_time(distance)
    if line == "3":
        return line3.calculate_time(distance)
    if line == "4":
        return line4.calculate_time(distance)


def get_coord(line, distance):
    if line == "1":
        return line1.calculate_coordinate(distance)
    if line == "2":
        return line2.calculate_coordinate(distance)
    if line == "3":
        return line3.calculate_coordinate(distance)
    if line == "4":
        return line4.calculate_coordinate(distance)


# 站点坐标
location_dic = {
    "樱海湖站": Coordinate(1629, 395),
    "阅海居站": Coordinate(1550, 500),
    "敬贤大道东口站": Coordinate(2112, 1017),
    "会文广场站": Coordinate(2554, 2295),
    "淦昌苑站": Coordinate(2153, 2630),
    "图书馆站": Coordinate(1623, 2630),
    "华岗苑站": Coordinate(1140, 2889),
    "振声苑站3": Coordinate(1248, 3241),
    "振声苑站4": Coordinate(1366, 3333),
    "博物馆站": Coordinate(1521, 3333),
    "第周苑站": Coordinate(2153, 3333),
    "曦园餐厅站": Coordinate(2630, 4050),
    "乐水居步行街东口站": Coordinate(540, 1480),
    "地铁山东大学站": Coordinate(235, 1685),
    "乐水居步行街西口站": Coordinate(235, 1480),
    "乐水居北区西门站": Coordinate(235, 477),
}


# 路线1
line1 = Route()
line1.add_ordered_coordinate(location_dic["阅海居站"])
line1.add_ordered_coordinate(Coordinate(1972, 500))
line1.add_ordered_coordinate(location_dic["敬贤大道东口站"])
line1.add_ordered_coordinate(Coordinate(2554, 2224))
line1.add_ordered_coordinate(location_dic["会文广场站"])
line1.add_ordered_coordinate(Coordinate(2554, 2630))
line1.add_ordered_coordinate(location_dic["淦昌苑站"])
line1.add_ordered_coordinate(location_dic["图书馆站"])
line1.add_ordered_coordinate(Coordinate(1181, 2630))
line1.add_ordered_coordinate(location_dic["华岗苑站"])
line1.add_ordered_coordinate(Coordinate(1089, 3333))
line1.add_ordered_coordinate(location_dic["博物馆站"])
line1.add_ordered_coordinate(location_dic["第周苑站"])
line1.add_ordered_coordinate(Coordinate(2630, 3333))
line1.add_ordered_coordinate(location_dic["曦园餐厅站"])


# 路线2
line2 = Route()
line2.add_ordered_coordinate(location_dic["樱海湖站"])
line2.add_ordered_coordinate(Coordinate(1619, 64))
line2.add_ordered_coordinate(Coordinate(235, 64))
line2.add_ordered_coordinate(location_dic["乐水居北区西门站"])
line2.add_ordered_coordinate(location_dic["乐水居步行街西口站"])
line2.add_ordered_coordinate(location_dic["地铁山东大学站"])
line2.add_ordered_coordinate(Coordinate(540, 1685))
line2.add_ordered_coordinate(location_dic["乐水居步行街东口站"])
line2.add_ordered_coordinate(Coordinate(540, 122))
line2.add_ordered_coordinate(Coordinate(1619, 122))
line2.add_ordered_coordinate(Coordinate(1619, 500))
line2.add_ordered_coordinate(Coordinate(1972, 500))
line2.add_ordered_coordinate(location_dic["敬贤大道东口站"])
line2.add_ordered_coordinate(location_dic["会文广场站"])
line2.add_ordered_coordinate(Coordinate(2554, 2630))
line2.add_ordered_coordinate(location_dic["淦昌苑站"])
line2.add_ordered_coordinate(location_dic["图书馆站"])
line2.add_ordered_coordinate(Coordinate(1181, 2630))
line2.add_ordered_coordinate(location_dic["华岗苑站"])
line2.add_ordered_coordinate(Coordinate(1089, 3333))
line2.add_ordered_coordinate(location_dic["博物馆站"])
line2.add_ordered_coordinate(location_dic["第周苑站"])
line2.add_ordered_coordinate(Coordinate(2630, 3333))
line2.add_ordered_coordinate(location_dic["曦园餐厅站"])


# 路线3
line3 = Route()
line3.add_ordered_coordinate(location_dic["阅海居站"])
line3.add_ordered_coordinate(Coordinate(1010, 500))
line3.add_ordered_coordinate(Coordinate(1124, 3034))
line3.add_ordered_coordinate(Coordinate(1248, 3034))
line3.add_ordered_coordinate(location_dic["振声苑站3"])


# 路线4
line4 = Route()
line4.add_ordered_coordinate(location_dic["振声苑站4"])
line4.add_ordered_coordinate(Coordinate(2630, 3333))
line4.add_ordered_coordinate(location_dic["曦园餐厅站"])


if __name__ == "__main__":
    C = line1.calculate_coordinate(3000)
    print(C)
