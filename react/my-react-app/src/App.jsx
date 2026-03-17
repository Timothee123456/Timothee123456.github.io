import React, { useState, useEffect } from 'react';
import { Play, Phone, Settings, User, Power, X, Check, Home, PhoneOff, Plus } from 'lucide-react';

const SmartHub = () => {
  const [isOn, setIsOn] = useState(true);
  const [isEditing, setIsEditing] = useState(false);
  
  // All available contacts (more than just the side buttons)
  const [allContacts, setAllContacts] = useState([
    'Sarah', 'Arthur', 'Cameron', 'Emma', 'Lucas', 'Chloe', 'Thomas', 'Lea'
  ]);
  
  // Side buttons: each can be a contact name or null (meaning no contact assigned)
  const [sideButtons, setSideButtons] = useState(['Sarah', 'Arthur', 'Cameron']);
  
  // Temporary state for editing
  const [tempAllContacts, setTempAllContacts] = useState([...allContacts]);
  const [tempSideButtons, setTempSideButtons] = useState([...sideButtons]);
  const [newContactName, setNewContactName] = useState('');

  const [currentPage, setCurrentPage] = useState('home'); // 'home', 'media', 'calls'
  const [movieIndex, setMovieIndex] = useState(0);
  const [currentCallContact, setCurrentCallContact] = useState(null); // name of contact being called
  const [callTimer, setCallTimer] = useState(0);

  const togglePower = () => {
    setIsOn(!isOn);
    if (isOn) {
      // Turning off: reset any active call
      setCurrentCallContact(null);
      setCallTimer(0);
    }
  };

  const handleEditStart = () => {
    // Initialize temp state with current values
    setTempAllContacts([...allContacts]);
    setTempSideButtons([...sideButtons]);
    setNewContactName('');
    setIsEditing(true);
  };

  const handleAddContact = () => {
    if (newContactName.trim() && !tempAllContacts.includes(newContactName.trim())) {
      setTempAllContacts([...tempAllContacts, newContactName.trim()]);
      setNewContactName('');
    }
  };

  const handleSideButtonChange = (index, value) => {
    const newSideButtons = [...tempSideButtons];
    newSideButtons[index] = value === '' ? null : value;
    setTempSideButtons(newSideButtons);
  };

  const handleSave = () => {
    setAllContacts([...tempAllContacts]);
    setSideButtons([...tempSideButtons]);
    setIsEditing(false);
  };

  const startCall = (contact) => {
    if (!isOn || !contact) return;
    setCurrentCallContact(contact);
    setCurrentPage('calls');
    setCallTimer(0);
  };

  const endCall = () => {
    setCurrentCallContact(null);
    setCallTimer(0);
  };

  // Movie data for the slideshow
  const movies = [
    { title: 'The Shawshank Redemption', image: 'https://picsum.photos/id/1015/400/600' },
    { title: 'The Godfather', image: 'https://picsum.photos/id/1043/400/600' },
    { title: 'Pulp Fiction', image: 'https://picsum.photos/id/106/400/600' },
    { title: 'Inception', image: 'https://picsum.photos/id/42/400/600' },
    { title: 'Fight Club', image: 'https://picsum.photos/id/96/400/600' },
    { title: 'Forrest Gump', image: 'https://picsum.photos/id/20/400/600' },
  ];

  // Auto‑advance the slideshow every 3 seconds when on the media page
  useEffect(() => {
    if (!isOn || currentPage !== 'media') return;
    const interval = setInterval(() => {
      setMovieIndex((prev) => (prev + 1) % movies.length);
    }, 3000);
    return () => clearInterval(interval);
  }, [isOn, currentPage, movies.length]);

  // Call timer effect
  useEffect(() => {
    if (!isOn || !currentCallContact) return;
    const interval = setInterval(() => {
      setCallTimer((prev) => prev + 1);
    }, 1000);
    return () => clearInterval(interval);
  }, [isOn, currentCallContact]);

  const formatTime = (seconds) => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  };

  return (
    <div className="flex items-center justify-center min-h-screen bg-slate-900 p-4 font-sans">
      {/* Main Device Frame */}
      <div className="relative w-full max-w-4xl aspect-[4/3] bg-zinc-800 rounded-3xl shadow-2xl border-8 border-zinc-700 overflow-hidden flex">
        
        {/* Screen Area */}
        <div className={`flex-1 relative transition-all duration-700 ${isOn ? 'bg-slate-50' : 'bg-black'}`}>
          {isOn && (
            <div className="h-full flex flex-col p-8">
              {/* Top Navigation */}
              <div className="flex justify-between items-center mb-12">
                <div className="flex gap-6 text-slate-400">
                  <button
                    onClick={() => setCurrentPage('home')}
                    className="w-8 h-8 rounded-full bg-slate-200 flex items-center justify-center hover:bg-slate-300 transition-colors"
                  >
                    <Home className="text-slate-600" />
                  </button>
                  <div className="flex gap-4 items-center">
                    <span className="text-xl">{"<"}</span>
                    <span className="text-xl">{">"}</span>
                  </div>
                </div>
                <button 
                  onClick={handleEditStart}
                  className="p-2 hover:bg-slate-200 rounded-full transition-colors"
                >
                  <Settings className="text-slate-600" />
                </button>
              </div>

              {/* Conditional Page Content */}
              {currentPage === 'home' && (
                /* Home Page */
                <>
                  <div className="flex-1 flex justify-around items-center gap-8 px-4">
                    <div 
                      className="flex flex-col items-center gap-4 group cursor-pointer"
                      onClick={() => {
                        setCurrentPage('media');
                        setMovieIndex(0);
                      }}
                    >
                      <div className="w-48 h-32 rounded-3xl border-2 border-slate-300 flex items-center justify-center group-hover:bg-slate-100 transition-all shadow-sm">
                        <Play size={48} fill="currentColor" className="text-slate-800 ml-2" />
                      </div>
                      <span className="text-2xl font-bold tracking-widest text-slate-700 uppercase">Medias</span>
                    </div>

                    <div 
                      className="flex flex-col items-center gap-4 group cursor-pointer"
                      onClick={() => {
                        setCurrentPage('calls');
                        setCurrentCallContact(null);
                      }}
                    >
                      <div className="w-48 h-32 rounded-3xl border-2 border-slate-300 flex items-center justify-center group-hover:bg-slate-100 transition-all shadow-sm">
                        <Phone size={48} className="text-slate-800" />
                      </div>
                      <span className="text-2xl font-bold tracking-widest text-slate-700 uppercase">Appels</span>
                    </div>
                  </div>

                  <div className="mt-auto pt-8">
                    <h1 className="text-4xl font-light text-slate-800 text-center" style={{ fontFamily: 'Brush Script MT, cursive' }}>Bonjour, <span className="font-medium">John</span></h1>
                  </div>
                </>
              )}

              {currentPage === 'media' && (
                <div className="flex-1 flex flex-col items-center justify-center">
                  <h2 className="text-2xl font-bold text-slate-800 mb-6">Films populaires</h2>
                  <div className="relative w-64 h-80">
                    {movies.map((movie, idx) => (
                      <div
                        key={idx}
                        className={`absolute inset-0 transition-opacity duration-1000 ease-in-out ${
                          idx === movieIndex ? 'opacity-100' : 'opacity-0'
                        }`}
                      >
                        <img
                          src={movie.image}
                          alt={movie.title}
                          className="w-full h-64 object-cover rounded-xl shadow-lg"
                        />
                        <p className="mt-4 text-lg font-medium text-slate-700 text-center">
                          {movie.title}
                        </p>
                      </div>
                    ))}
                  </div>
                  <p className="text-xs text-slate-500 mt-8">Lecture automatique • Sans fin</p>
                </div>
              )}

              {currentPage === 'calls' && (
                <div className="flex-1 flex flex-col">
                  {currentCallContact ? (
                    /* Active call screen */
                    <div className="flex-1 flex flex-col items-center justify-center gap-8">
                      <div className="w-32 h-32 rounded-full bg-slate-300 flex items-center justify-center">
                        <User size={64} className="text-slate-600" />
                      </div>
                      <div className="text-center">
                        <h2 className="text-3xl font-bold text-slate-800">{currentCallContact}</h2>
                        <p className="text-2xl font-mono text-slate-600 mt-2">{formatTime(callTimer)}</p>
                        <p className="text-sm text-slate-500 mt-1">En communication</p>
                      </div>
                      <button
                        onClick={endCall}
                        className="mt-8 bg-red-500 hover:bg-red-600 text-white p-4 rounded-full shadow-lg flex items-center gap-2 transition-all"
                      >
                        <PhoneOff size={24} />
                        <span className="font-bold">Raccrocher</span>
                      </button>
                    </div>
                  ) : (
                    /* Contact list */
                    <div className="flex-1 flex flex-col">
                      <h2 className="text-2xl font-bold text-slate-800 mb-6">Choisir un contact</h2>
                      <div className="space-y-4 overflow-y-auto">
                        {allContacts.map((contact, index) => {
                          // Check if this contact is assigned to a side button
                          const isOnSideButton = sideButtons.includes(contact);
                          return (
                            <button
                              key={index}
                              onClick={() => startCall(contact)}
                              className="w-full flex items-center gap-4 p-4 bg-white rounded-xl shadow-sm hover:bg-slate-100 transition-colors border border-slate-200"
                            >
                              <div className="w-12 h-12 rounded-full bg-slate-300 flex items-center justify-center">
                                <User size={24} className="text-slate-600" />
                              </div>
                              <span className="text-xl font-medium text-slate-700">{contact}</span>
                              {isOnSideButton && (
                                <span className="ml-auto text-xs bg-blue-100 text-blue-700 px-2 py-1 rounded-full">
                                  Raccourci
                                </span>
                              )}
                            </button>
                          );
                        })}
                      </div>
                    </div>
                  )}
                </div>
              )}

              {/* Edit Modal */}
              {isEditing && (
                <div className="absolute inset-0 bg-white/95 backdrop-blur-sm z-20 p-12 flex flex-col overflow-y-auto">
                  <div className="flex justify-between items-center mb-8">
                    <h2 className="text-2xl font-bold text-slate-800">Configurer les boutons</h2>
                    <button onClick={() => setIsEditing(false)}><X /></button>
                  </div>

                  <div className="space-y-6">
                    <div>
                      <h3 className="text-lg font-semibold text-slate-700 mb-4">Boutons latéraux</h3>
                      {[0, 1, 2].map((idx) => (
                        <div key={idx} className="mb-4">
                          <label className="block text-sm font-medium text-slate-600 mb-1">
                            Bouton {idx + 1}
                          </label>
                          <select
                            value={tempSideButtons[idx] || ''}
                            onChange={(e) => handleSideButtonChange(idx, e.target.value)}
                            className="w-full p-3 bg-slate-100 rounded-xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-blue-500"
                          >
                            <option value="">— Aucun —</option>
                            {tempAllContacts.map((contact) => (
                              <option key={contact} value={contact}>
                                {contact}
                              </option>
                            ))}
                          </select>
                        </div>
                      ))}
                    </div>

                    <div className="border-t pt-6">
                      <h3 className="text-lg font-semibold text-slate-700 mb-4">Ajouter un nouveau contact</h3>
                      <div className="flex gap-2">
                        <input
                          type="text"
                          value={newContactName}
                          onChange={(e) => setNewContactName(e.target.value)}
                          placeholder="Nom du contact"
                          className="flex-1 p-3 bg-slate-100 rounded-xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-blue-500"
                          onKeyPress={(e) => e.key === 'Enter' && handleAddContact()}
                        />
                        <button
                          onClick={handleAddContact}
                          className="px-4 py-2 bg-blue-600 text-white rounded-xl hover:bg-blue-700 transition-colors flex items-center gap-2"
                        >
                          <Plus size={20} />
                          Ajouter
                        </button>
                      </div>
                    </div>

                    <div className="border-t pt-6">
                      <h3 className="text-lg font-semibold text-slate-700 mb-4">Tous les contacts</h3>
                      <ul className="space-y-2 max-h-40 overflow-y-auto">
                        {tempAllContacts.map((contact) => (
                          <li key={contact} className="flex items-center gap-2 p-2 bg-slate-50 rounded">
                            <User size={16} className="text-slate-400" />
                            <span>{contact}</span>
                          </li>
                        ))}
                      </ul>
                    </div>
                  </div>

                  <button 
                    onClick={handleSave}
                    className="mt-8 w-full bg-slate-800 text-white p-4 rounded-xl font-bold flex items-center justify-center gap-2"
                  >
                    <Check size={20} /> Enregistrer les modifications
                  </button>
                </div>
              )}
            </div>
          )}
        </div>

        {/* Side Button Panel – now uses sideButtons state */}
        <div className="w-32 bg-zinc-800 flex flex-col items-center py-12 gap-8 border-l border-zinc-700">
          {sideButtons.map((contact, i) => (
            <div key={i} className="flex flex-col items-center gap-2">
              <button 
                onClick={() => startCall(contact)}
                disabled={!isOn || !contact}
                className={`w-20 h-14 rounded-xl shadow-lg flex items-center justify-center transition-all active:scale-95 ${
                  isOn && contact
                    ? 'bg-zinc-100 text-zinc-800 hover:bg-zinc-200' 
                    : 'bg-zinc-900 text-zinc-700 cursor-not-allowed'
                }`}
              >
                <span className="text-xs font-bold uppercase tracking-tighter truncate px-1">
                  {contact || '---'}
                </span>
              </button>
            </div>
          ))}

          {/* Power Button */}
          <div className="mt-auto mb-4 flex flex-col items-center gap-2">
            <button 
              onClick={togglePower}
              className={`w-20 h-20 rounded-full flex flex-col items-center justify-center transition-all border-4 shadow-inner
                ${isOn 
                  ? 'bg-green-500/10 border-green-500 text-green-500 shadow-green-500/20' 
                  : 'bg-zinc-900 border-zinc-700 text-zinc-600'}`}
            >
              <Power size={24} className={isOn ? 'animate-pulse' : ''} />
              <span className="text-[10px] font-bold mt-1">ON/OFF</span>
            </button>
          </div>
        </div>
      </div>

      {/* Instructions */}
      <div className="absolute bottom-8 text-slate-400 text-sm max-w-md text-center">
        Ceci est une version interactive avec une liste de contacts élargie. 
        Cliquez sur l'icône <Settings className="inline w-4 h-4" /> pour assigner les boutons latéraux parmi tous vos contacts,
        ou ajouter de nouveaux contacts. La page "Appels" affiche désormais tous les contacts.
      </div>
    </div>
  );
};

export default SmartHub;