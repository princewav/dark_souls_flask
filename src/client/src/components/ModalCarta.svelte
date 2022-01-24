<script>
  import CartaModificabile from './CartaModificabile.svelte';
  import { createEventDispatcher } from 'svelte';
  import { savedCards } from '../stores.js';

  export let cardData = '{}';
  let { id, type, ...card } = JSON.parse(cardData);

  const dispatch = createEventDispatcher();
  function closeCardModal() {
    dispatch('closecardmodal');
  }
  function saveCard() {
    dispatch('save', $savedCards);
  }
</script>

<div class="modal-container">
  <div class="modal">
    <h1>Crea Carta</h1>
    <h3>{id}</h3>
    <div class="card">
      <CartaModificabile {id} {card} />
    </div>

    <div class="flex">
      <images class="ds-btn" on:click={closeCardModal}>ESCI</images>
      <images class="ds-btn" on:click={saveCard}>CREA</images>
    </div>

    <div class="legenda">
      <p>N = Dado Nero</p>
      <p>B = Dado Blu</p>
      <p>A = Dado Arancio</p>
      <p>O = Nodo</p>
      <p>P = Portata 0</p>
      <p>M = Magico</p>
      <p>U = Muovi</p>
    </div>
  </div>
</div>

<style>
  .modal-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(48, 48, 48, 0.925);
    z-index: 40;
  }

  .modal {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background: #efe4d8;
    box-shadow: inset 0 0 10px 9px #afa18f;
    border: 5px solid #655641;
    border-radius: 20px;
    width: 60%;
    min-width: 430px;
    max-width: 650px;
    height: 600px;
    text-align: center;
    font-family: 'cinzel', serif;
    padding: 20px 50px;
  }

  .card {
    width: 300px;
    height: 390px;
    margin: 5px auto 32px auto;
  }

  .flex {
    display: flex;
    justify-content: space-evenly;
    justify-content: space-evenly;
  }

  .legenda {
    position: absolute;
    top: 50%;
    right: 10px;
    transform: translateY(-50%);
    text-align: start;
  }
  .legenda p {
    font-family: 'cinzel', serif;
    font-weight: bold;
  }
</style>
