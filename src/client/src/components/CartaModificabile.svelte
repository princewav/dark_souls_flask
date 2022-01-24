<script>
  import { createEventDispatcher, afterUpdate } from 'svelte';
  import { isEmpty, getNextEl, getPrevEl, dropLast, drop, closest } from '../utils.js';
  import { savedCards } from '../stores.js';

  export let id = '';
  export let card = {};

  card = !isEmpty(card)
    ? card
    : {
        portata: 0,
        impugnatura: 1,
        nome: 'Nuova Carta',
        immagine: '',
        forza: 0,
        destrezza: 0,
        intelligenza: 0,
        fede: 0,
        attacchi: [{ costo: 0, icone: [] }],
        scudo: { valore: 1, colore: 'nero' },
        contrasto: { valore: 0, colore: '' },
        schivata: 0,
        potenziamenti: 0
      };

  $: card.immagine = card.immagine.toLowerCase().replace(' ', '_');

  afterUpdate(() => {
    savedCards.set(JSON.stringify({ id, ...card }));
  });

  const dispatch = createEventDispatcher();
  function openCardModal() {
    dispatch('opencardmodal', cardData);
  }

  const toggleImpugnatura = () => {
    card.impugnatura = card.impugnatura === 2 ? 1 : 2;
  };

  // TODO gestire il muovi con il numerino dentro
  const clearEmptyInputs = e => {
    if (e.target.matches('input[type=number]') && e.target.value === '0') e.target.value = '';
  };

  const sequenzaColori = ['nero', 'blu', 'arancio', ''];
  const cambiaDado = (segno, prop) => {
    if (prop === 'scudo') {
      card.scudo.colore =
        segno === '+'
          ? getNextEl(sequenzaColori, card.scudo.colore)
          : getPrevEl(sequenzaColori, card.scudo.colore);
    } else {
      card.contrasto.colore =
        segno === '+'
          ? getNextEl(sequenzaColori, card.contrasto.colore)
          : getPrevEl(sequenzaColori, card.contrasto.colore);
    }
  };
  const cambiaAttacchi = segno => {
    const defaultAtk = { costo: 0, icone: [] };
    if (segno === '+') {
      if (card.attacchi.length < 3) card.attacchi = [...card.attacchi, defaultAtk];
    } else {
      if (card.attacchi.length > 1) card.attacchi = dropLast(card.attacchi);
    }
  };
  const rimuoviIcona = (icone, i, j) => {
    icone = drop(icone, j);
    card.attacchi[i] = { ...card.attacchi[i], icone };
  };

  let selectedAtk;
  let selectedAtkIndex;
  const toggleAttaccoSelezionato = e => {
    selectedAtk = closest(e.target, 'tr');
    selectedAtkIndex = [...closest(e.target, '.attacchi').querySelectorAll('tr')].indexOf(
      selectedAtk
    );
    closest(e.target, '.attacchi')
      .querySelectorAll('tr')
      .forEach(el => {
        if (el !== selectedAtk) el.classList.remove('selected-atk');
      });
    selectedAtk.classList.toggle('selected-atk');
  };

  const incrementIcon = img => {
    const noIncrementIcons = ['portata0', 'magico', 'nodo'];
    let current = card.attacchi[selectedAtkIndex].icone
      .filter(ico => ico.immagine === img)
      .map(ico => ({ ...ico, valore: ico.valore + (noIncrementIcons.includes(img) ? 0 : 1) }));

    if (isEmpty(current)) {
      card.attacchi[selectedAtkIndex].icone = [
        ...card.attacchi[selectedAtkIndex].icone,
        { immagine: img, valore: noIncrementIcons.includes(img) ? 0 : 1 }
      ];
    } else {
      card.attacchi[selectedAtkIndex].icone = [
        ...card.attacchi[selectedAtkIndex].icone.filter(ico => ico.immagine !== img),
        ...current
      ];
    }
  };
  const appendIcon = e => {
    switch (e.key.toLowerCase()) {
      case 'n':
        incrementIcon('dado nero');
        break;
      case 'b':
        incrementIcon('dado blu');
        break;
      case 'a':
        incrementIcon('dado arancio');
        break;
      case 'o':
        incrementIcon('nodo');
        break;
      case 'p':
        incrementIcon('portata0');
        break;
      case 'm':
        incrementIcon('magico');
        break;
      case 'u':
        incrementIcon('muovi');
        break;
    }
  };
</script>

<svelte:window on:keydown={appendIcon} />
<div class="blocco" on:click={clearEmptyInputs}>
  {#if !isEmpty(card)}
    <div class="carta">
      <div class="cerchio portata">
        <img src="images/portata.png" width="27" height="27" alt="portata" />
        <input type="number" bind:value={card.portata} placeholder="0" />
      </div>
      <div class="nome">
        <textarea bind:value={card.nome} />
      </div>
      <div class="cerchio impugnatura" on:click={toggleImpugnatura}>
        <img src="images/{card.impugnatura}_mano.png" width="45" height="45" alt="impugnatura" />
      </div>
      <div class="livelli">
        <div class="forza">
          <img src="images/simbolo-forza.png" alt="forza" />
          <input type="number" bind:value={card.forza} placeholder="0" />
        </div>
        <div class="destrezza">
          <img src="images/simbolo-destrezza.png" alt="destrezza" />
          <input type="number" bind:value={card.destrezza} placeholder="0" />
        </div>
        <div class="intelligenza">
          <img src="images/simbolo-intelligenza.png" alt="intelligenza" />
          <input type="number" bind:value={card.intelligenza} placeholder="0" />
        </div>
        <div class="fede">
          <img src="images/simbolo-fede.png" alt="fede" />
          <input type="number" bind:value={card.fede} placeholder="0" />
        </div>
      </div>
      <div class="immagine">
        <input type="text" bind:value={card.immagine} placeholder="Immagine" />
        {#if card.immagine}
          <img
            src="https://darksouls3.wiki.fextralife.com/file/Dark-Souls-3/{card.immagine}.png"
            alt="immagine"
            height="80" />
        {/if}
      </div>
      <div class="attacchi" on:click={toggleAttaccoSelezionato}>
        <table>
          {#each card.attacchi as attacco, i}
            <tr>
              <td>
                <input type="text" value="[{attacco.costo}]" />
              </td>
              <td class="attacco">
                {#each attacco.icone as icona, j}
                  <div class="icona" on:click={() => rimuoviIcona(attacco.icone, i, j)}>
                    <img src="images/{icona.immagine}.png" alt={icona.immagine} />
                    {#if icona.valore}
                      <span class="valore {icona.immagine === 'muovi' ? 'muovi' : ''}">
                        {icona.valore}
                      </span>
                    {/if}
                  </div>
                {/each}
              </td>
            </tr>
          {/each}
        </table>
        <div class="modifica-attacchi">
          <div class="mod-btn" on:click={() => cambiaAttacchi('-')}>−</div>
          <div class="mod-btn" on:click={() => cambiaAttacchi('+')}>+</div>
        </div>
      </div>
      <div class="difesa scudo">
        <img src="images/scudo.png" alt="scudo" />
        {#if card.scudo.colore}
          <img class="dado" src="images/dado {card.scudo.colore}.png" alt="dado scudo" />
        {/if}
        <span class="valore {card.scudo.colore ? '' : 'no-dado'}">
          <input type="number" bind:value={card.scudo.valore} placeholder="0" />
        </span>
        <div class="modifica-dadi">
          <div class="mod-btn" on:click={() => cambiaDado('-', 'scudo')}>−</div>
          <div class="mod-btn" on:click={() => cambiaDado('+', 'scudo')}>+</div>
        </div>
      </div>
      <div class="difesa contrasto">
        <img src="images/contrasto.png" alt="contrasto" />
        {#if card.contrasto.colore}
          <img class="dado" src="images/dado {card.contrasto.colore}.png" alt="dado contrasto" />
        {/if}
        <span class="valore {card.contrasto.colore ? '' : 'no-dado'}">
          <input type="number" bind:value={card.contrasto.valore} placeholder="0" />
        </span>
        <div class="modifica-dadi">
          <div class="mod-btn" on:click={() => cambiaDado('-', 'contrasto')}>−</div>
          <div class="mod-btn" on:click={() => cambiaDado('+', 'contrasto')}>+</div>
        </div>
      </div>
      <div class="cerchio schivata" alt="schivata">
        <img src="images/schivata.png" alt="dado schivata" />
        <span class="valore">
          <input type="number" bind:value={card.schivata} placeholder="0" />
        </span>
      </div>
      <div class="cerchio potenziamenti" alt="potenziamenti">
        <img src="images/potenziamenti.png" alt="dado potenziamenti" />
        <span class="valore">
          <input type="number" bind:value={card.potenziamenti} placeholder="0" />
        </span>
      </div>
    </div>
  {/if}
</div>

<style>
  :root {
    --circle-size: 55px;
  }

  input[type='text'],
  input[type='number'],
  textarea {
    background: none;
    border: none;
    color: inherit;
    width: 100%;
    text-align: inherit;
    font-family: inherit;
    font-size: inherit;
    font-weight: inherit;
    outline: none;
  }
  textarea {
    resize: none;
  }
  input[type='number'] {
    -moz-appearance: textfield;
  }
  input::-webkit-outer-spin-button,
  input::-webkit-inner-spin-button {
    -webkit-appearance: none;
    margin: 0;
  }

  .blocco {
    width: -webkit-fill-available;
    height: -webkit-fill-available;
  }

  .cerchio {
    width: var(--circle-size);
    height: var(--circle-size);
    background: #efe4d8;
    box-shadow: inset 0 0 10px 9px #afa18f;
    border: 2px solid #655641;
    border-radius: 50%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-around;
    line-height: 1;
    color: black;
    font-weight: bold;
  }

  .cerchio img {
    max-width: 98%;
  }

  .carta {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    grid-template-rows: 1fr 1fr 1fr 2fr 1fr;
    height: 100%;
    grid-template-areas:
      'portata  nome      nome     impugnatura'
      'livelli  immagine  immagine immagine'
      'livelli  immagine  immagine immagine'
      'attacchi attacchi  attacchi attacchi'
      'scudo    contrasto schivata potenziamenti';
    text-align: center;
    background: linear-gradient(45deg, #040b11, #2c373d);
    border-radius: 7px;
    padding: 5px;
    transition: transform 0.2s ease-out;
    position: relative;
    z-index: 2;
    -webkit-user-select: none;
    font-size: 16px;
    font-weight: bold;
  }

  .carta > div {
    margin: 3px;
  }
  .carta > .cerchio,
  .carta > .difesa {
    margin: 0;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }

  .portata {
    grid-area: portata;
  }
  .nome {
    grid-area: nome;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-weight: normal;
  }
  .impugnatura {
    grid-area: impugnatura;
  }
  .livelli {
    grid-area: livelli;
    background: #efe4d8;
    box-shadow: inset 0 0 10px 9px #afa18f;
    border: 2px solid #655641;
    padding: 1px 2px 0 3px;
    padding-bottom: 2px;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
  }
  .livelli > div {
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-bottom: 1px #65564159 dashed;
  }
  .livelli > div:last-child {
    border-bottom: none;
  }

  .livelli img {
    width: 46%;
    padding-right: 3px;
    padding-bottom: 3px;
    border-right: 1px #65564159 dashed;
  }
  .immagine {
    grid-area: immagine;
    color: white;
    font-size: 13px;
  }

  .attacchi {
    grid-area: attacchi;
    background: #efe4d8;
    box-shadow: inset 0 0 10px 9px #afa18f;
    border: 2px solid #655641;
    position: relative;
  }
  .attacchi table {
    width: 100%;
    height: 100%;
    font-size: 17px;
  }
  .attacchi table td:first-child {
    width: 32px;
    border-right: 1px dashed #65564159;
  }
  .attacchi table tr:not(:last-child) td {
    border-bottom: 1px dashed #65564159;
  }

  .attacchi .attacco {
    display: flex;
    align-items: center;
    height: 100%;
  }
  .attacchi .icona {
    position: relative;
    width: 38px;
    margin-right: 5px;
  }
  .attacchi .icona img {
    width: 100%;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }
  .attacchi .icona .valore {
    color: white;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }
  .muovi {
    color: black !important;
    font-size: 14px;
  }

  .scudo {
    grid-area: scudo;
    position: relative;
  }

  .difesa {
    width: var(--circle-size);
    height: var(--circle-size);
  }

  .difesa > img {
    width: 100%;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }
  .difesa .dado {
    width: 70%;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    z-index: 2;
  }
  .difesa .valore {
    position: absolute;
    z-index: 2;
    font-size: 18px;
    color: white;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }
  .no-dado.valore {
    color: black;
  }

  .contrasto {
    grid-area: contrasto;
    position: relative;
  }
  .contrasto > img {
    width: 100%;
  }
  .contrasto .dado {
    width: 70%;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    z-index: 2;
  }
  .schivata {
    grid-area: schivata;
    position: relative;
  }
  .schivata input {
    text-align: right;
  }
  .schivata img {
    width: 77%;
    position: absolute;
    bottom: 0;
    left: 50%;
    transform: translate(-50%, 0);
  }
  .schivata .valore {
    color: black;
    position: absolute;
    top: 9px;
    right: 8px;
    z-index: 2;
    font-size: 16px;
  }
  .potenziamenti {
    grid-area: potenziamenti;
    position: relative;
  }
  .potenziamenti img {
    width: 98%;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }
  .potenziamenti .valore {
    color: white;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -36%);
    z-index: 2;
    font-size: 18px;
  }
  .modifica-dadi {
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: absolute;
    bottom: -18px;
    width: 100%;
    margin: auto;
    left: 50%;
    transform: translateX(-50%);
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
  }
  .mod-btn:hover {
    background: rgba(224, 224, 224, 0.774);
  }
  .mod-btn:active {
    background: rgba(255, 255, 255, 0.931);
  }

  .modifica-attacchi {
    display: flex;
    justify-content: flex-end;
    align-items: center;
    position: absolute;
    bottom: -5px;
    width: fit-content;
    right: 0;
  }
</style>
