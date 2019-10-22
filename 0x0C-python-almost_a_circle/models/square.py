#!/usr/bin/python3
'''this class inherits from rectangle'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''inherits from Rectangle'''
    def __init__(self, size, x=0, y=0, id=None):
        '''method init use method of the super class'''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''this method set the size'''
        return self.width

    @size.setter
    def size(self, value):
        '''this method the size'''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''update arguments of the square'''
        args_sq = []
        for idx in range(len(args)):
            if idx == 0:
                args_sq.append(args[idx])
            elif idx == 1:
                args_sq.append(args[idx])
                args_sq.append(args[idx])
            elif idx == 2:
                args_sq.append(args[idx])
            elif idx == 3:
                args_sq.append(args[idx])

        if len(kwargs) != 0:
            kwargs_cp = kwargs.copy()
            for key in kwargs_cp:
                if key == "size":
                    kwargs["width"] = kwargs[key]
                    kwargs["height"] = kwargs[key]

        super().update(*args_sq, **kwargs)

    def __str__(self):
        ''' return the information of a object'''
        return '[{}] ({}) {}/{} - {}'
        .format(__class__.__name__, self.id, self.x, self.y,
                self.size)

    def to_dictionary(self):
        '''return a dictionay of attributes and arguments'''
        return {'x': self.x, 'y': self.y, 'id': self.id, 'height': self.height,
                'width': self.width}
