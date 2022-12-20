<script lang="ts" setup>
import PButton from 'primevue/button';

import { solveMultiQueuingTheoryWithRejection } from '~~/services/multiple_queue_channel_with_rejection';
definePageMeta({ title: 'Single', layout: 'main' })
const average_time = ref('')
const intensity = ref('')
const number_of_channels = ref('')
const result_data = ref([])
const show = ref(false)

const solve_queue_parameters = async () => {
    const result = await solveMultiQueuingTheoryWithRejection(parseFloat(average_time.value), parseFloat(intensity.value), parseInt(number_of_channels.value))
    result_data.value = result.data["multi_channel_queuing_theory_solution"]
    show.value = true
}


</script>



<template>
    <div>
        <h1 class="italic m-b-10">Многоканальная СМО с отказами</h1>
        <div class="average_time m-t-5">
            <h5 class="m-b-1">Интенсивность оформления заявок в минуту</h5>
            <div class="p-inputgroup w-40%">
                <span class="p-inputgroup-addon">
                    <i class="pi pi-globe text-[#060E28]"></i>
                </span>
                <InputText placeholder="Интенсивность оформления заявок в минуту" v-model="average_time" />
            </div>
        </div>
        <div class="intensity m-t-5">
            <h5 class="m-b-1">Интенсивность поступления заявок</h5>
            <div class="p-inputgroup w-40%">
                <span class="p-inputgroup-addon">
                    <i class="pi pi-globe text-[#060E28]"></i>
                </span>
                <InputText placeholder="Интенсивность поступления заявок" v-model="intensity" />
            </div>
        </div>
        <div class="number_of_channels m-t-5">
            <h5 class="m-b-1">Количество каналов</h5>
            <div class="p-inputgroup w-40%">
                <span class="p-inputgroup-addon">
                    <i class="pi pi-globe text-[#060E28]"></i>
                </span>
                <InputText placeholder="Количество каналов" v-model="number_of_channels" />
            </div>
        </div>
        <PButton label="Результат" class="bg-[#060E28] b-[#060E28] m-t-5" @click="solve_queue_parameters" />
        <div v-if="show" class="data_table m-t-7 p-5">
            <DataTable :value="result_data" :paginator="true" :rows="10" :rowsPerPageOptions="[10, 20, 50]"
                :responsive="true">
                <Column field="description" header="Имя колонки" />
                <Column field="value" header="Значение" />
            </DataTable>
        </div>
    </div>
</template>