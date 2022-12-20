class MultiChannelQuery:
    def __fac(self, n):
        if n == 0:
            return 1
        return self.__fac(n-1) * n
 
    def __calculate_p_0(self,intensity, number_of_channels, average_time):
        p_0 = 0
        for i in range(number_of_channels+1):
            p_0 += (intensity**i)/(self.__fac(i)*average_time**i)
        return 1/p_0
    
    def get_multi_queuing_theory_solution(self, intensity, number_of_channels, average_time):
        downtime_probability = self.__calculate_p_0(intensity, number_of_channels, average_time)
        failure_probability = ((intensity/average_time)**3)*downtime_probability/self.__fac(number_of_channels)
        relative_throughput = 1-failure_probability
        absolute_bandwidth = intensity*relative_throughput
        average_busy_channels = absolute_bandwidth/average_time

        answer = {
            "downtime_probability": {
                "value": str(downtime_probability)[:5],
                "description": "Вероятность простоя системы"
            },
            "failure_probability": {
                "value": str(failure_probability)[:5],
                "description": "Вероятность отказа"
            },
            "relative_throughput": {
                "value": str(relative_throughput)[:5],
                "description": "Относительная пропускная способность"
            },
            "absolute_bandwidth": {
                "value": str(absolute_bandwidth)[:5],
                "description": "Абсолютная пропускная способность"
            },
            "average_busy_channels": {
                "value": str(average_busy_channels)[:5],
                "description": "Среднее число занятых каналов"
            }
            }
        return answer



