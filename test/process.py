import numpy 

class FactoryProcess : 

    def __init__(self) : 
        self.output = 0 

    def step(self, input_rate) : 
        
        
class Process : 
    '''Simulate a control process with a selectable PID controller and factory
process functions''' 

    def __init__(self, pid, setpoint, steps, **kwargs) :
        self.pid = pid 

        # Generate the setpoint stimulus
        self.steps = steps
        self.setpoint = numpy.resize([1], (self.steps,))
        self.setpoint[0] = 0
        self.setpoint[1] = 0
        self.setpoint *= setpoint 
        
        # Create the output arrays 
        self.feedback = numpy.resize([], self.setpoint.shape)
        self.output = numpy.resize([], self.setpoint.shape)

        if 'factory_function' not in kwargs : 
            self.factory_func = lambda x : x 
        else:
            self.factory_func = kwargs['factory_function']

        if 'output_filter' not in kwargs : 
            self.output_filter = lambda x : x 
        else:
            self.output_filter = kwargs['output_filter'] 

    def run(self) :         
        output = 0 
        feedback = 0
        for x, point in enumerate(self.sp) : 
            feedback = self.factory_func(output)
            self.output[x,] = output 
            self.feedback[x,] = feedback
            output = self.output_filter(self.pid.step(point, feedback))
            
