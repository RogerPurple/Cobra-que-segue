import pygame
import utils
from utils import Vector


class Segment():
    def __init__(self, __position: Vector, _direction: Vector) -> None:
        self.position = __position
        self.tam = 10
        self.dir = _direction
        
    def move(self, dir_x, dir_y, dir_normalized):
        self.position.x += dir_x
        self.position.y += dir_y
        self.dir = dir_normalized
        
class Cobra():
    def __init__(self, __position: Vector, _num_segments: int, _distance_segments: int, _speed=2.5) -> None:
        self.num_segments = _num_segments
        self.position = __position
        
        self.segments = [None] * _num_segments
        self.distance_segments = _distance_segments
        self.speed = _speed

        for idx in range(len(self.segments)):
            self.segments[idx] = Segment(Vector(self.position.x - (self.distance_segments * idx), self.position.y), Vector(1, 0))
            
    def update(self, _mouse_pos):
        _mouse_dir = Vector(_mouse_pos[0], _mouse_pos[1])
        direction = utils.dir(_mouse_dir, self.segments[0].position)
        self.segments[0].position.x += direction.x * self.speed
        self.segments[0].position.y += direction.y * self.speed
        
        for idx in range(1, len(self.segments)):
            direction = utils.dir(self.segments[idx-1].position, self.segments[idx].position)
            distance = utils.distance(self.segments[idx-1].position, self.segments[idx].position)
            
            self.segments[idx].move(distance.x - self.distance_segments * direction.x, distance.y - self.distance_segments * direction.y, direction )
        
        return None
    
    def add_segment(self):
        last_segment = self.segments[-1]
        _vect = Vector(
            last_segment.position.x - last_segment.dir.x * self.distance_segments, 
            last_segment.position.y - last_segment.dir.y * self.distance_segments)
        
        new_segment = Segment(_vect, last_segment.dir)
        self.segments.append(new_segment)
        del _vect

    def remove_segment(self):
        self.segments.pop()
        
        
