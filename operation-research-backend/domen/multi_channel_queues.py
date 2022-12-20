class MultiChannelQueueWithRejection:
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



class MultiChannelQueueWithExpectation:
    def __fac(self, n):
        if n == 0:
            return 1
        return self.__fac(n-1) * n

    def __intensity(self, requests_flow_rate, service_flow_rate):
        return requests_flow_rate/service_flow_rate

    def __calculate_p_0(self, intensity, number_of_channels):
        p_0 = 0
        for i in range(number_of_channels):
            p_0 += (intensity**i)/self.__fac(i)
        p_0 += intensity**number_of_channels/(self.__fac(number_of_channels)*(1-(intensity/number_of_channels)))
        return 1/p_0
    
    def __calculate_probabilities(self, intensity, number_of_channels):
        p_0 = self.__calculate_p_0(intensity,number_of_channels)
        busy_probabilities_of_channels = {}
        for i in range(1, number_of_channels+1):
            if f'channel_{i}' not in busy_probabilities_of_channels:
                busy_probabilities_of_channels[f'channel_{i}'] = {}
            busy_probabilities_of_channels[f'channel_{i}']["description"] = f'Вероятность того, что обслуживанием: занят {i} канал'
            busy_probabilities_of_channels[f'channel_{i}']["value"] = round(((intensity**i)/self.__fac(i))*p_0,20)
        return busy_probabilities_of_channels

    def __average_amount_of_busy_channels(self,intensity):
        return intensity

    def __calculate_busy_coefficient(self, average_amount_of_busy_channels, number_of_channels):
        return average_amount_of_busy_channels/number_of_channels
    
    def __queue_formation_probability(self, intensity, number_of_channels):
        return ((intensity**(number_of_channels+1))/(self.__fac(number_of_channels)*(number_of_channels-intensity)))*self.__calculate_p_0(intensity, number_of_channels)

    def __probability_of_no_queue(self, queue_formation_probability):
        return 1-queue_formation_probability

    def __queue_average_number_request(self, number_of_channels, intensity, queue_formation_probability):
        return number_of_channels/(number_of_channels-intensity)*queue_formation_probability

    def __average_downtime(self, queue_average_number_request,requests_flow_rate):
        return queue_average_number_request/requests_flow_rate

    def get_multi_queuing_theory_solution(self, requests_flow_rate, service_flow_rate, number_of_channels):
        intensity = self.__intensity(requests_flow_rate, service_flow_rate)
        p_0 = self.__calculate_p_0(intensity, number_of_channels)
        busy_probabilities_of_channels = self.__calculate_probabilities(intensity, number_of_channels)
        average_amount_of_busy_channels = self.__average_amount_of_busy_channels(intensity)
        busy_coefficient = self.__calculate_busy_coefficient(average_amount_of_busy_channels, number_of_channels)
        queue_formation_probability = self.__queue_formation_probability(intensity, number_of_channels)
        probability_of_no_queue = self.__probability_of_no_queue(queue_formation_probability)
        queue_average_number_request = self.__queue_average_number_request(number_of_channels, intensity, queue_formation_probability)
        average_downtime = self.__average_downtime(queue_average_number_request, requests_flow_rate)

        answer = {
            "intensity": {
                "value": str(intensity)[:5],
                "description": "Интенсивность нагрузки"
            },
            "p_0": {
                "value": str(p_0)[:5],
                "description": "Вероятность, что канал свободен"
            },
            "busy_probabilities_of_channels": {
                "value": busy_probabilities_of_channels,
                "description": "Вероятность занятости каналов"
            },
            "rejection_probability": {
                "value": str(0),
                "description": "Вероятность отказа"
            },
            "average_amount_of_busy_channels": {
                "value": str(average_amount_of_busy_channels)[:5],
                "description": "Среднее число занятых каналов"
            },
            "busy_coefficient": {
                "value": str(busy_coefficient)[:5],
                "description": "Коэффициент занятости"
            },
            "queue_formation_probability": {
                "value": str(queue_formation_probability)[:5],
                "description": "Вероятность очереди"
            },
            "probability_of_no_queue": {
                "value": str(probability_of_no_queue)[:5],
                "description": "Вероятность отсутствия очереди"
            },
            "queue_average_number_request": {
                "value": str(queue_average_number_request)[:5],
                "description": "Среднее число заявок в очереди"
            },
            "average_downtime": {
                "value": str(average_downtime)[:5],
                "description": "Среднее время простоя"
            }
            }

        return answer