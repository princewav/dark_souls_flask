<script>
  import CartaModificabile from './CartaModificabile.svelte';
  import { createEventDispatcher, afterUpdate } from 'svelte';
  import { savedPowerup } from '../stores.js';
  import { regex, capitalize, isEmpty } from '../utils.js';

  export let powerupData = '{}';
  let { id, type, ...powerup } = JSON.parse(powerupData);

  let [powerupType, powerupNum] = regex('pot-(\\w+)(\\d)', id);
  powerupType = capitalize(
    powerupType === 'dx' ? 'destra' : powerupType === 'sx' ? 'sinistra' : powerupType
  );

  powerup = isEmpty(powerup)
    ? { immagine: '', descrizione: '', icona: { tipo: '', valore: 0 } }
    : powerup;

  let src;
  $: powerup.immagine = powerup.immagine.toLowerCase().replace(' ', '_');
  $: src = powerup.immagine
    ? `https://darksouls3.wiki.fextralife.com/file/Dark-Souls-3/${powerup.immagine}.png`
    : '';

  afterUpdate(() => {
    savedPowerup.set(JSON.stringify({ id, ...powerup }));
  });

  const tipiIcona = [
    '',
    'dado nero',
    '+',
    'veleno',
    'sanguinamento',
    'magico',
    'congelamento',
    'vacillamento'
  ];

  const cambiaValoreIcona = segno => {
    if (segno === '+') {
      powerup.icona.valore += 1;
    } else {
      if (powerup.icona.valore > 1) powerup.icona.valore -= 1;
    }
  };

  const dispatch = createEventDispatcher();
  function closePowerupModal() {
    dispatch('closepowerupmodal');
  }
  function savePowerup() {
    dispatch('save', $savedPowerup);
  }
</script>

<div class="modal-container">
  <div class="modal">
    <h1>Crea Potenziamento</h1>
    <h3>Potenziamento {powerupType !== 'Armatura' ? 'arma ' : ''}{powerupType} n° {powerupNum}</h3>
    <div class="potenziamento">

      <p>Immagine</p>
      <div class="image">
        <input type="text" placeholder="Immagine" bind:value={powerup.immagine} />
        <div class="img-container">
          {#if src}
            <img {src} alt="Powerup" />
          {/if}
        </div>
      </div>

      <p>Descrizione</p>
      <textarea class="descrizione" bind:value={powerup.descrizione} />

      <p>Icona</p>
      <div class="icona">
        <select bind:value={powerup.icona.tipo}>
          {#each tipiIcona as tipo}
            <option value={tipo}>{capitalize(tipo)}</option>
          {/each}
        </select>

        <div style="position: relative">
          {#if powerup.icona.tipo === '+'}
            <span class="valore-piu">+ {powerup.icona.valore}</span>
          {:else if powerup.icona.tipo !== ''}
            <img src="images/{powerup.icona.tipo}.png" width="60" height="60" alt="s" />
            {#if powerup.icona.tipo === 'dado nero'}
              <span class="valore">{powerup.icona.valore}</span>
            {/if}
          {/if}
        </div>

        {#if ['+', 'dado nero'].includes(powerup.icona.tipo)}
          <div class="modifica-attacchi">
            <div class="mod-btn" on:click={() => cambiaValoreIcona('-')}>−</div>
            <div class="mod-btn" on:click={() => cambiaValoreIcona('+')}>+</div>
          </div>
        {/if}
      </div>
    </div>

    <div class="flex">
      <images class="ds-btn" on:click={closePowerupModal}>ESCI</images>
      <images class="ds-btn" on:click={savePowerup}>CREA</images>
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
    width: fit-content;
    height: fit-content;
    text-align: center;
    font-family: 'cinzel', serif;
    padding: 30px;
  }

  .flex {
    display: flex;
    justify-content: space-evenly;
    justify-content: space-evenly;
  }

  .potenziamento {
    margin: 15px 0;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
  }

  input[type='text'],
  textarea,
  select {
    border: 1px solid #655641;
    color: black;
    text-align: inherit;
    font-family: inherit;
    font-size: inherit;
    font-weight: bold;
    outline: none;
    background: #4545451a;
    padding: 5px;
    border-radius: 6px;
    margin: 5px;
    margin-bottom: 15px;
  }

  .img-container {
    background: #4545451a;
    width: 120px;
    height: 132px;
    padding: 10px;
    margin: auto;
    border-radius: 6px;
    border: 1px solid #655641;
  }

  .image img {
    width: 100%;
    height: 100%;
  }

  .descrizione {
    overflow: hidden;
    resize: none;
    margin: 10px;
    height: 110px;
    width: 280px;
  }

  .icona {
    width: 100px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  .icona .valore {
    position: absolute;
    color: white;
    font-size: 2em;
    font-weight: bold;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }
  .icona .valore-piu {
    color: black;
    font-size: 2em;
    font-weight: bold;
    position: relative;
  }

  .modifica-attacchi {
    display: flex;
    justify-content: space-evenly;
    width: 100%;
    align-items: center;
  }

  .mod-btn {
    background: white;
    border: 1px solid #655641;
    width: 20px;
    height: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 4px;
    transition: background 0.3s ease;
    cursor: pointer;
    user-select: none;
  }
  .mod-btn:hover {
    background: rgba(224, 224, 224, 0.774);
  }
  .mod-btn:active {
    background: rgba(255, 255, 255, 0.931);
  }

  p {
    font-family: 'cinzel', serif;
    font-weight: bold;
    font-size: 1.2em;
  }

  .image,
  .descrizione,
  .icona {
    margin-bottom: 20px;
  }
</style>
