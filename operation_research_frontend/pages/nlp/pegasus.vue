<script lang="ts" setup>
import Textarea from 'primevue/textarea';
import PButton from 'primevue/button';
import { paraphraseInRussian, paraphraseInEnglish } from '~~/services/paraphrase_ru';
import ProgressSpinner from 'primevue/progressspinner';
import Dropdown from 'primevue/dropdown';
definePageMeta({ title: 'Pegasus', layout: 'main' })

const text = ref('')
const result = ref('')
const isLoad = ref(false)
const selectedLanguage = ref(null)
const languages = [
    { name: 'English', code: 'EN' },
    { name: 'Russian', code: 'RU' }
]

const paraphrase = async () => {
    isLoad.value = true

    var data = []
    data.push(text.value)

    if (selectedLanguage.value.name == 'English') {
        await paraphraseInEnglish(data).then((res) => {
            result.value = res.data["paraphrased_data"]
        })
    } else {
        await paraphraseInRussian(data).then((res) => {
            result.value = res.data["paraphrased_data"]
        })
    }
    isLoad.value = false
}


</script>


<template>
    <div class="flex flex-col items-center justify-between">
        <h1 class="m-b-10">Парафрайзер</h1>
        <div class="flexjustify-around">
            <div class="flex flex-col items-center">
                <div class="flex flex-col items-center">
                    <h4 class="m-b-1">Ввдедите текст. А мы его перефразируем.</h4>
                    <Textarea v-model="text" rows="10" cols="50" />
                    <Dropdown class="m-t-3" v-model="selectedLanguage" :options="languages" optionLabel="name"
                        placeholder="Выберите язык" />
                </div>
                <div class="flex flex-col items-center">
                    <PButton label="Результат" class="bg-[#060E28] b-[#060E28] m-t-3" @click="paraphrase" />
                </div>
            </div>

            <div class="result b w-100% b-dashed m-t-5 p-10 p-t-5">
                <h3 class="font-bold italic m-b-3 mt-3">Результат:</h3>

                <ProgressSpinner v-if="isLoad" />

                <p class="italic">{{ result }}</p>
            </div>
        </div>



    </div>
</template>