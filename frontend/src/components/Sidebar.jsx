import { useLocation } from 'react-router-dom'

function Sidebar() {

  const location = useLocation()

  // MAIN DASHBOARD ONLY

  const isMainDashboard = location.pathname === '/'

  return (

    <aside className="w-[220px] fixed left-0 top-0 h-screen bg-[#081726] border-r border-cyan-400/20 p-5 z-50">

      {/* LOGO */}

      <div>

        <h1 className="text-3xl font-bold text-yellow-400">

          Telecom AI

        </h1>

        <p className="text-sm text-cyan-300 uppercase tracking-[4px] mt-3 leading-7">

          Intelligence Platform

        </p>

      </div>

      {/* BUTTONS */}

      <div className="mt-16 space-y-5">

        {/* OVERVIEW */}

        <button onClick={() => {

            if (window.location.pathname === '/') {

            const section = document.getElementById('overview')

            if (section) {

                section.scrollIntoView({
                behavior: 'smooth'
                })

            }

            } else {

            window.location.href = '/'

            }

        }}

        className="
            w-full
            py-5
            rounded-3xl
            font-bold
            text-lg
            transition-all
            duration-300
            bg-yellow-400
            text-black
            hover:scale-[1.03]
            cursor-pointer
        "
        >

            Overview

        </button>

        {/* RISK */}

        <button onClick={() => {

            if (window.location.pathname === '/') {

            const section = document.getElementById('risk-table')

            if (section) {

                section.scrollIntoView({
                behavior: 'smooth'
                })

            }

            } else {

            window.location.href = '/'

            }

        }}

        className="
            w-full
            py-5
            rounded-3xl
            text-lg
            border
            transition-all
            duration-300
            bg-[#0B1B2B]
            border-cyan-400/20
            hover:border-cyan-300
            hover:scale-[1.03]
            cursor-pointer
        "
        >

            Risk Intelligence

        </button>
      </div>


    </aside>
  )
}

export default Sidebar