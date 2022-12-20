class SingleChannelQueue:

    def __flow_rate(self, t):
        return 1/t

    def __system_load_factor(self, lambda_value, flow_rate):
        return lambda_value/flow_rate

    def __relative_throughput(self, flow_rate, lambda_value):
        return flow_rate/(flow_rate+lambda_value)

    def __absolute_bandwidth(self, lambda_value, relative_throughput):
        return lambda_value * relative_throughput

    def __failure_probability(self, relative_throughput):
        return 1-relative_throughput

    def get_single_queuing_theory_solution(self, lambda_value, t):
        answer = [ 
            {
                "value": str(self.__flow_rate(t))[:5],
                "description": "Интенсивность потока обслуживания"
            }, 
            {
                "value": str(self.__system_load_factor(lambda_value, self.__flow_rate(t)))[:5],
                "description": "Коэффициент загрузки системы"
            }, 
            {
                "value": str(self.__relative_throughput(self.__flow_rate(t), lambda_value))[:5],
                "description": "Относительная пропускная способность"
            },
            {
                "value": str(self.__absolute_bandwidth(lambda_value, self.__relative_throughput(self.__flow_rate(t), lambda_value)))[:5],
                "description": "Абсолютная пропускная способность"
            },
             {
                "value": str(self.__failure_probability(self.__relative_throughput(self.__flow_rate(t), lambda_value)))[:5],
                "description": "Вероятность отказа"
            }
        ]

        return answer
    

