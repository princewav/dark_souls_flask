<script>
  import { createEventDispatcher } from 'svelte';
  import { post } from '../utils.js';
  let slots = [{ name: 'SalcyPrincy', date: '04/06/2020', time: '16:34' }];
  let openLoadModal = false;
  let openSaveAsModal = false;
  let saveAsName = '';
  let lastSaved = '';
  let slotToLoad = '';

  const dispatch = createEventDispatcher();
  async function openLoad() {
    const res = await fetch('/slots');
    slots = (await res.json()) || [];
    openLoadModal = true;
  }
  function saveAs() {
    let date = new Date().toLocaleDateString();
    let time = new Date().toLocaleTimeString();
    let payload = { ...window.localStorage, saveAsName, date, time };
    post('save_as', payload);
    dispatch('saveas', { saveAsName });
    lastSaved = saveAsName;
    openSaveAsModal = false;
    alert(`Saved "${lastSaved}"!`);
  }
  async function deleteSlot(name) {
    const confirmation = confirm('Vuoi davvero eliminare ' + name + '?');
    if (confirmation) {
      post('delete_slot', { name });
      const res = await fetch('/slots');
      slots = (await res.json()) || [];
    }
  }
  async function loadMatch(name) {
    const res = await fetch('/load_match/' + name);
    let matchData = (await res.json()) || [];
    dispatch('loadedGame', { matchData });
    openLoadModal = false;
    lastSaved = name;
    saveAsName = name;
  }
</script>

<div class="container">
  {#if openLoadModal}
    <div class="modal-container">
      <div class="modal">
        <h1>Scegli slot partita:</h1>
        <div class="slot-container">
          {#each slots as slot, i}
            <div
              class="slot"
              on:click={() => {
                loadMatch(slot.name);
              }}
            >
              <img src="images/warrior_pic.png" height="70" alt="pic" />
              <div class="slot-info">
                <p class="slot-name">{slot.name}</p>
                <p>Ultimo salvataggio:</p>
                <p>{slot.date} - {slot.time}</p>
              </div>
              <div
                class="small-btn delete"
                on:click|stopPropagation={() => {
                  deleteSlot(slot.name);
                }}
              >
                ×
              </div>
            </div>
          {/each}
        </div>
        <div class="btn-container">
          <button class="ds-btn" on:click={() => (openLoadModal = false)}>Esci</button>
        </div>
      </div>
    </div>
  {/if}
  {#if openSaveAsModal}
    <div class="modal-container">
      <div class="modal">
        <h1>Salva come:</h1>
        <p class="label">Nome slot salvataggio</p>
        <input type="text" bind:value={saveAsName} />
        <div class="btn-container">
          <button class="ds-btn" on:click={() => (openSaveAsModal = false)}>Esci</button>
          <button class="ds-btn" on:click={saveAs}>Salva</button>
        </div>
      </div>
    </div>
  {/if}
  <h1>Salvataggio</h1>
  {#if lastSaved}
    <h5>
      Salvataggio attivo:
      <span>{lastSaved}</span>
    </h5>
  {:else}
    <h5>Nessun salvataggio attivo</h5>
  {/if}
  <div class="btn-container">
    <button class="ds-btn" on:click={saveAs} disabled={lastSaved.length == 0}>Salva</button>
    <button class="ds-btn" on:click={() => (openSaveAsModal = true)}>Salva come</button>
    <button class="ds-btn" on:click={openLoad}>Carica</button>
  </div>
</div>

<style>
  .container {
    background: #efe4d8;
    box-shadow: inset 0 0 10px 9px #afa18f;
    border: 5px solid #655641;
    border-radius: 20px;
    width: 100%;
    text-align: center;
    font-family: 'cinzel', serif;
    padding: 30px;
    font-size: 1.4em;
  }

  .btn-container {
    display: flex;
    justify-content: space-evenly;
    align-items: center;
  }

  h5 {
    color: #655641;
    margin: 15px;
  }
  h5 span {
    font-weight: bold;
    font-size: 1.1em;
    color: black;
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
    text-align: center;
    font-family: 'cinzel', serif;
    padding: 20px 50px;
    z-index: 100;
  }
  .modal-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(48, 48, 48, 0.925);
    z-index: 40;
  }
  .slot-container {
    margin-bottom: 15px;
    max-height: 500px;
    overflow: scroll;
    padding-right: 10px;
  }

  .slot {
    border: 1px solid #655641;
    margin: 5px;
    padding: 5px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-radius: 6px;
    cursor: pointer;
    transition: 0.3s all;
    user-select: none;
  }
  .slot img {
    border-radius: 6px;
  }
  .slot-info {
    font-size: 0.7em;
  }
  .slot-name {
    font-family: 'cinzel', serif;
    font-weight: bold;
    font-size: 1.2em;
  }
  .slot:hover {
    background: #ffad5145;
  }
  .slot:active {
    background: #dd7c0c45;
  }
  input {
    padding: 6px;
    text-align: center;
    background: #0000002b;
    border: none;
    font-family: 'cinzel', serif;
    font-size: 17px;
    font-weight: bold;
    margin-bottom: 15px;
    border-radius: 4px;
  }
  p.label {
    font-family: 'cinzel', serif;
    font-size: 0.8em;
  }
</style>
