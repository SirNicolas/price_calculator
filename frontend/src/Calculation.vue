<template>
  <v-content>
    <v-container fluid fill-height>
      <v-layout align-center justify-center>
        <v-flex xs12 sm8 md4>
          <v-card class="elevation-12">
            <v-toolbar dark color="primary">
              <v-toolbar-title>{{ appName }}</v-toolbar-title>
              <v-spacer></v-spacer>
            </v-toolbar>
            <v-card-text>
              <v-form @keyup.enter="submit">
                <v-text-field @keyup.enter="submit" v-model="quantity" name="quantity" label="Quantity" type="quantity"
                              id="number"></v-text-field>
                <v-text-field @keyup.enter="submit" v-model="price" name="price_per_item" label="Price" id="price"
                              type="number"></v-text-field>
                <v-text-field @keyup.enter="submit" v-model="state" name="state" label="State" id="state"
                              type="text"></v-text-field>
                <v-text-field @keyup.enter="submit" v-model="discount" name="discount" label="discount" id="discount"
                              type="text"></v-text-field>
                <v-text-field @keyup.enter="submit" v-model="priceWithDiscount" name="priceWithDiscount"
                              label="priceWithDiscount" id="priceWithDiscount" type="text"></v-text-field>
                <v-text-field @keyup.enter="submit" v-model="tax" name="tax" label="tax" id="tax"
                              type="text"></v-text-field>
                <v-text-field @keyup.enter="submit" v-model="stateTax" name="stateTax" label="stateTax" id="stateTax"
                              type="text"></v-text-field>
                <v-text-field @keyup.enter="submit" v-model="finalPrice" name="finalPrice" label="finalPrice"
                              id="finalPrice" type="text"></v-text-field>
              </v-form>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn @click.prevent="submit">Calculate</v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </v-content>
</template>

<script lang="ts">
import {Component, Vue} from 'vue-property-decorator';
import {apiUrl, appName} from '@/env';
import axios from 'axios';

export interface ICalculate {
  quantity: number;
  price_per_item: number;
  state: string;
}


@Component
export default class Calculation extends Vue {
  public quantity: number = 0;
  public price: number = 0;
  public state: string = 'CA';
  public discount: number = 0;
  public priceWithDiscount: number = 0;
  public tax: number = 0;
  public stateTax: number = 0;
  public finalPrice: number = 0;
  public appName = appName;

  public update(response) {
    this.discount = response.data.discount;
    this.priceWithDiscount = response.data.price_with_discount;
    this.tax = response.data.tax;
    this.stateTax = response.data.state_tax;
    this.finalPrice = response.data.final_price;
  }
  public submit() {
    const data: ICalculate = {
      quantity: this.quantity,
      price_per_item: this.price,
      state: this.state,
    };
    axios
        .post(`${apiUrl}/api/v1/calculation`, data)
        .then((response) => (
            this.update(response)
        ));
  }
}
</script>

<style>
</style>
