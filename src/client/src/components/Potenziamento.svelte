<script>
  import { createEventDispatcher } from 'svelte';
  import { isEmpty } from '../utils.js';
  export let id;
  export let type;
  export let powerup = {};

  const dispatch = createEventDispatcher();
  function openAddPowerupModal() {
    dispatch('add', { id, type });
  }
  function openEditPowerupModal() {
    dispatch('edit', { id, type, ...powerup });
  }
</script>

<div class="blocco {id}">
  {#if isEmpty(powerup)}
    <img src="images/potenziamento-{type}.png" alt="potenziamento-{type}" class="bg-icon" />
    <div class="small-btn-container">
      <div class="small-btn add" on:click={openAddPowerupModal}>+</div>
    </div>
  {:else}
    <div class="powerup-container">
      <img
        class="immagine"
        src="https://darksouls3.wiki.fextralife.com/file/Dark-Souls-3/{powerup.immagine}.png"
        alt="powerup img" />
      <span class="descrizione-powerup">{powerup.descrizione}</span>
      <div class="icona">
        {#if powerup.icona.tipo === '+'}
          <span class="valore-piu">+{powerup.icona.valore}</span>
        {:else if powerup.icona.tipo !== ''}
          <img src="images/{powerup.icona.tipo}.png" width="40" height="40" alt="s" />
          {#if powerup.icona.tipo === 'dado nero'}
            <span class="valore">{powerup.icona.valore}</span>
          {/if}
        {/if}
      </div>
    </div>
    <div class="small-btn-container right">
      <div class="small-btn delete" on:click={() => (powerup = {})}>×</div>
      <div class="small-btn edit" on:click={openEditPowerupModal}>M</div>
    </div>
  {/if}
</div>

<style>
  .bg-icon {
    width: 45px;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }

  .add {
    background: rgb(0, 132, 255);
  }
  .add:active {
    background: rgb(0, 60, 255);
    transform: scale(1.2);
  }

  .powerup-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 100%;
    padding-left: 5px;
  }
  .immagine {
    width: 40px;
    height: 40px;
  }
  .icona {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-right: 20px;
    padding: 5px;
  }
  .icona .valore {
    position: absolute;
    color: white;
    font-size: 1.4em;
    font-weight: bold;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }
  .icona .valore-piu {
    color: black;
    font-size: 1.4em;
    font-weight: bold;
    position: relative;
    width: 28px;
    display: inline-block;
  }
  .descrizione-powerup {
    font-size: 12px;
    line-height: 12px;
    padding: 5px;
    padding-right: 0;
    font-weight: bold;
    text-align: center;
  }
  .right {
    margin-right: -13px;
  }
</style>
