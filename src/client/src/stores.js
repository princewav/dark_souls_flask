import { writable } from 'svelte/store';

export const savedCards = writable('{}');
export const savedPowerups = writable('{}');
export const savedPowerupsAsObjects = writable({});