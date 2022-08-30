import '../styles/globals.css'
import type { AppProps } from 'next/app'
import Timer from '../components/timer';
import RoundToNearest15 from '../utils/RoundToNearest15';


function MyApp({ Component, pageProps }: AppProps) {
  return (
    <div>
      <Timer initialMinute={RoundToNearest15(new Date())}/>
      <Component {...pageProps} />
    </div>
  )
}

export default MyApp
