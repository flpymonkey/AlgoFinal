from glm import vec2, normalize
import pyray as ray
from BSPTree import BSPTreeBuilder
from BSPTreeTraverser import BSPTreeTraverser
from settings import MAP_HEIGHT, MAP_WIDTH, MAP_OFFSET


class View:
    def __init__(self, segments, BSPTree: BSPTreeBuilder,
                 BSPTraverser: BSPTreeTraverser):
        self.BSPTree = BSPTree
        self.BSPTraverser = BSPTraverser
        raw_segments = [seg.position for seg in segments]
        bounds = self.get_bounds(raw_segments)
        self.x_min, self.y_min, self.x_max, self.y_max = bounds
        #
        self.raw_segments = self.remap_array(raw_segments)
        #
        self.segments = self.remap_array(
            [seg.position for seg in segments])
        self.counter = 0.0

    def draw(self):
        self.draw_raw_segments()
        self.draw_segments()
        self.draw_player()
        self.counter += 0.0005

    def draw_player(self):
        x0, y0 = self.remap_vec2(self.BSPTraverser.cam_pos)
        ray.draw_circle_v((x0, y0), 10, ray.GREEN)

    def draw_segments(self, seg_color=ray.ORANGE):
        segment_ids = self.BSPTraverser.seg_ids_to_draw
        #
        # for seg_id in segment_ids:
        for seg_id in segment_ids[:int(self.counter) % (len(segment_ids) + 1)]:
            (x0, y0), (x1, y1) = p0, p1 = self.segments[seg_id]
            #
            ray.draw_line_v((x0, y0), (x1, y1), seg_color)
            self.draw_normal(p0, p1, seg_color)
            #
            ray.draw_circle_v((x0, y0), 3, ray.WHITE)

    def draw_normal(self, p0, p1, color, scale=12):
        p10 = p1 - p0
        normal = normalize(vec2(-p10.y, p10.x))
        n0 = (p0 + p1) * 0.5
        n1 = n0 + normal * scale
        #
        ray.draw_line_v((n0.x, n0.y), (n1.x, n1.y), color)

    def draw_raw_segments(self):
        for p0, p1 in self.raw_segments:
            (x0, y0), (x1, y1) = p0, p1
            ray.draw_line_v((x0, y0), (x1, y1), ray.DARKGRAY)

    def remap_array(self, arr: list[tuple[vec2]]):
        return [(self.remap_vec2(p0), self.remap_vec2(p1)) for p0, p1 in arr]

    def remap_vec2(self, p: vec2):
        x = self.remap_x(p.x)
        y = self.remap_y(p.y)
        return vec2(x, y)

    def remap_x(self, x, out_min=MAP_OFFSET, out_max=MAP_WIDTH):
        return ((x - self.x_min) * (out_max - out_min)
                / (self.x_max - self.x_min) + out_min)

    def remap_y(self, y, out_min=MAP_OFFSET, out_max=MAP_HEIGHT):
        return ((y - self.y_min) * (out_max - out_min)
                / (self.y_max - self.y_min) + out_min)

    @staticmethod
    def get_bounds(segments: list[tuple[vec2]]):
        inf = float('inf')
        x_min, y_min, x_max, y_max = inf, inf, -inf, -inf
        #
        for p0, p1 in segments:
            x_min = p0.x if p0.x < x_min else p1.x if p1.x < x_min else x_min
            x_max = p0.x if p0.x > x_max else p1.x if p1.x > x_max else x_max
            #
            y_min = p0.y if p0.y < y_min else p1.y if p1.y < y_min else y_min
            y_max = p0.y if p0.y > y_max else p1.y if p1.y > y_max else y_max
        return x_min, y_min, x_max, y_max
