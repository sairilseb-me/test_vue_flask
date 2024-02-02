<template>
    <v-container>
        <v-row>
            <v-col>
                <v-card>
                    <v-card-title>Test</v-card-title>
                    <v-card-text>
                        <v-btn color="primary" @click="test">Test 1</v-btn>
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>
        <v-row>
            <v-col>
                <v-card class="pa-4">
                    <v-form @submit.prevent="submit">
                        <v-card-title>Test Submit User</v-card-title>
                        <v-card-text>
                            <v-text-field label="Username" class="mb-2" v-model="form.username"></v-text-field>
                            <v-text-field label="Password" class="mb-2" v-model="form.password"></v-text-field>
                        </v-card-text>
                        <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn type="submit" color="primary" class="mb-2">Submit</v-btn>
                        </v-card-actions>
                    </v-form>
                   <v-divider></v-divider>
                    <v-card>
                        {{ result.username }}
                    </v-card>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import axios from 'axios'
import { ref } from 'vue'
export default {
    setup() {
        
        const form = ref({
            username: '',
            password: '',
        })

        const result = ref({})

        const test = () => {
            axios.get('http://127.0.0.1:5000/')
            .then(response => {
                console.log(response)
            })
        }

        const submit = () => {
            axios.post('http://127.0.0.1:5000/api/user', {username: form.value.username, password: form.value.password})
            .then(response => {
                
                result.value = response.data.data
            })
        }

        return {
            test,
            form,
            submit,
            result,
        }
    },
}
</script>